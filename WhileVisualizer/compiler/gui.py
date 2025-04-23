import tkinter as tk               
import customtkinter as ctk
from customtkinter import CTkFont, CTkTextbox, CTkFrame, CTkLabel, CTkButton, CTkScrollbar
from antlr4 import InputStream, CommonTokenStream, Token, ParseTreeWalker
from PIL import Image, ImageTk
import copy
import time
from graphviz import Source
import os
from io import StringIO
from tkinter import messagebox
import networkx as nx  
import re  


from grammar.WhileLexer import WhileLexer
from grammar.WhileParser import WhileParser
from compiler.IRGen import irgen
from CEmitter.CGen import CGen
from CEmitter.PythonGen import PythonGen


from simpleir.SimpleIRLexer import SimpleIRLexer
from simpleir.SimpleIRParser import SimpleIRParser
from compiler.Optimize import IRList, build_cfg, reconstruct_ir, dataflow_analysis, visualize_graph

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

optimize_ir = False
last_cfg = None
optimization_steps = []

def toggle_optimization():
    global optimize_ir, optimize_button
    optimize_ir = not optimize_ir
    if optimize_ir:
        optimize_button.configure(text="Optimization: ON", fg_color="#00AA00", hover_color="#00CC00")
    else:
        optimize_button.configure(text="Optimization: OFF", fg_color="#AA0000", hover_color="#CC0000")

def optimize_ir_code(ir_code):
    global last_cfg  
    try:
        lines = ir_code.strip().split('\n')
        if not lines:
            return ir_code

        header = None
        footer = []
        body = []
        for line in lines:
            if line.startswith("function "):
                header = line
            elif line.startswith("return ") or line.startswith("end function"):
                footer.append(line)
            elif not line.strip().startswith("#"):
                body.append(line)

        if not header:
            header = "function main"

        full_ir = header + "\n" + "\n".join(body) + "\n" + "\n".join(footer)
        parser = SimpleIRParser(CommonTokenStream(SimpleIRLexer(InputStream(full_ir))))
        tree = parser.unit()

        if parser.getNumberOfSyntaxErrors() > 0:
            optimized_lines = body
        else:
            walker = ParseTreeWalker()
            irl = IRList()
            walker.walk(irl, tree)
            instrs = irl.instr
            cfg = build_cfg(instrs)
            cfg = dataflow_analysis(cfg)
            last_cfg = cfg
            optimized_ir = reconstruct_ir(cfg)
            optimized_lines = [l for l in optimized_ir.strip().split('\n') if l.strip()]

        
        result = [header] + optimized_lines + footer
        return "\n".join(result)
    except Exception as e:
        return f"# Optimization error: {str(e)}\n{ir_code}"


def capture_optimization_steps(ir_code):
    global optimization_steps
    optimization_steps = []
    
    lexer = SimpleIRLexer(InputStream(ir_code))
    stream = CommonTokenStream(lexer)
    parser = SimpleIRParser(stream)
    tree = parser.unit()
    walker = ParseTreeWalker()
    irl = IRList()
    walker.walk(irl, tree)
    instrs = irl.instr
    
    text_instrs = []
    for instr in instrs:
        text_instrs.append(SimpleInstruction(instr.getText()))
    
    cfg = build_cfg(text_instrs)
    step1 = {
        'cfg': cfg,
        'description': "Initial CFG before optimization",
        'constants': {}
    }
    optimization_steps.append(step1)
    
    constants = {}
    for node in cfg.nodes:
        for instr in cfg.nodes[node].get("instrs", []):
            text = instr.getText()
            if ":=" in text and "goto" not in text:
                parts = text.split(":=", 1)
                lhs = parts[0].strip()
                rhs = parts[1].strip()
                if rhs.isdigit():
                    constants[lhs] = int(rhs)
    
    if constants:
        cfg2 = nx.DiGraph()
        for node in cfg.nodes:
            cfg2.add_node(node, instrs=cfg.nodes[node].get("instrs", []))
        for edge in cfg.edges:
            cfg2.add_edge(*edge)
            
        step2 = {
            'cfg': cfg2,
            'description': f"Constants identified: {constants}",
            'constants': dict(constants),
            'highlight_nodes': list(set(node for var in constants for node in find_nodes_with_var(cfg, var)))
        }
        optimization_steps.append(step2)
        
        for var, val in constants.items():
           
            affected_nodes = find_nodes_with_var(cfg, var)
            
            if affected_nodes:
                
                const_cfg = nx.DiGraph()
                for node in cfg.nodes:
                    const_cfg.add_node(node, instrs=[SimpleInstruction(i.getText()) for i in cfg.nodes[node].get("instrs", [])])
                for edge in cfg.edges:
                    const_cfg.add_edge(*edge)
                    
                step = {
                    'cfg': const_cfg,
                    'description': f"Propagated constant: {var} = {val}",
                    'constants': dict(constants),
                    'highlight_nodes': affected_nodes
                }
                optimization_steps.append(step)
    
    updated_cfg = nx.DiGraph()
    for node in cfg.nodes:
        
        updated_cfg.add_node(node, instrs=[SimpleInstruction(i.getText()) for i in cfg.nodes[node].get("instrs", [])])
    for edge in cfg.edges:
        
        updated_cfg.add_edge(*edge)
        
    for var, val in constants.items():
       
        affected_nodes = []
        for node in updated_cfg.nodes:
            for i, instr in enumerate(updated_cfg.nodes[node].get("instrs", [])):
                text = instr.getText()
                if var in text and ":=" in text and text.split(":=")[0].strip() != var:
                    new_text = text.replace(var, str(val))
                    updated_cfg.nodes[node]["instrs"][i] = SimpleInstruction(new_text)
                    affected_nodes.append(node)
        
        if affected_nodes:
            next_cfg = nx.DiGraph()
            for node in updated_cfg.nodes:
                next_cfg.add_node(node, instrs=[SimpleInstruction(i.getText()) for i in updated_cfg.nodes[node].get("instrs", [])])
            for edge in updated_cfg.edges:
                next_cfg.add_edge(*edge)
                
            step = {
                'cfg': next_cfg,
                'description': f"Propagated constant: {var} = {val}",
                'constants': dict(constants),
                'highlight_nodes': affected_nodes
            }
            optimization_steps.append(step)
    
    for node in updated_cfg.nodes:
        for i, instr in enumerate(updated_cfg.nodes[node].get("instrs", [])):
            text = instr.getText()
            if ":=" in text and any(op in text for op in ["+", "-", "*", "/"]):
                parts = text.split(":=", 1)
                lhs = parts[0].strip()
                rhs = parts[1].strip()
                
                match = re.match(r'(\d+)\s*([+\-*/])\s*(\d+)$', rhs)
                if match:
                    a, op, b = match.groups()
                    a, b = int(a), int(b)
                    
                    if op == '+': result = a + b
                    elif op == '-': result = a - b
                    elif op == '*': result = a * b
                    elif op == '/' and b != 0: result = a // b
                    else: continue
                    
                    new_text = f"{lhs} := {result}"
                    if new_text != text:
                        next_cfg = nx.DiGraph()
                        for n in updated_cfg.nodes:
                            next_cfg.add_node(n, instrs=[SimpleInstruction(i.getText()) for i in updated_cfg.nodes[n].get("instrs", [])])
                        for edge in updated_cfg.edges:
                            next_cfg.add_edge(*edge)
                            
                        next_cfg.nodes[node]["instrs"][i] = SimpleInstruction(new_text)
                        constants[lhs] = result
                        
                        step = {
                            'cfg': next_cfg,
                            'description': f"Evaluated expression: {rhs} = {result}",
                            'constants': dict(constants),
                            'highlight_nodes': [node]
                        }
                        optimization_steps.append(step)
                        
                        updated_cfg = next_cfg
    
    final_cfg = nx.DiGraph()
    for node in updated_cfg.nodes:
        final_cfg.add_node(node, instrs=[SimpleInstruction(i.getText()) for i in updated_cfg.nodes[node].get("instrs", [])])
    for edge in updated_cfg.edges:
        final_cfg.add_edge(*edge)
        
    step_final = {
        'cfg': final_cfg,
        'description': "Final optimized CFG",
        'constants': dict(constants)
    }
    optimization_steps.append(step_final)
    
    return optimization_steps


class SimpleInstruction:
    def __init__(self, text):
        self.text = text
        
    def getText(self):
        return self.text

def find_nodes_with_var(cfg, var):
    nodes = []
    for node in cfg.nodes:
        for instr in cfg.nodes[node].get("instrs", []):
            if var in instr.getText():
                nodes.append(node)
                break
    return nodes

def show_optimization_animation():
    try:
        
        input_text = editor.get("1.0", tk.END)
        in_stream = InputStream(input_text)
        ir_buf = StringIO()
        irgen(in_stream, ir_buf)
        ir_code = ir_buf.getvalue()
        
        
        steps = capture_optimization_steps(ir_code)
        if len(steps) <= 1:
            messagebox.showinfo("Optimization Animation", "No optimization steps to show!")
            return
            
        anim_win = ctk.CTkToplevel(root)
        anim_win.title("Optimization Animation")
        anim_win.geometry("800x700")
        anim_win.transient(root)
        anim_win.lift()
        
        
        top_frame = ctk.CTkFrame(anim_win)
        top_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        bottom_frame = ctk.CTkFrame(anim_win)
        bottom_frame.pack(fill="x", padx=10, pady=10)
        
        desc_label = ctk.CTkLabel(top_frame, text="", font=("Consolas", 14))
        desc_label.pack(pady=10)
        
        img_label = tk.Label(top_frame)
        img_label.pack(fill="both", expand=True, padx=10, pady=10)
        
        step_var = tk.IntVar(value=0)
        
        def update_display(event=None):
            step = step_var.get()
            if 0 <= step < len(steps):
                desc_label.configure(text=steps[step]['description'])
                
                cfg = steps[step]['cfg']
                highlight_nodes = steps[step].get('highlight_nodes', [])
                
                for node in cfg.nodes:
                    if node in highlight_nodes:
                        cfg.nodes[node]['highlight'] = True
                    else:
                        cfg.nodes[node]['highlight'] = False
                
                step_img = f"step_{step}.png"
                visualize_graph(cfg, filename=step_img)
                
                img = Image.open(step_img)
                img = img.resize((700, 500), Image.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                img_label.configure(image=photo)
                img_label.image = photo
                
                step_counter.configure(text=f"Step {step+1}/{len(steps)}")
        
        slider = ctk.CTkSlider(
            bottom_frame,
            from_=0,
            to=len(steps)-1,
            number_of_steps=len(steps)-1,
            command=update_display,
            variable=step_var
        )
        slider.pack(fill="x", padx=20, pady=10, side="left", expand=True)
        
        step_counter = ctk.CTkLabel(bottom_frame, text=f"Step 1/{len(steps)}")
        step_counter.pack(side="right", padx=10)
        
        def prev_step():
            if step_var.get() > 0:
                step_var.set(step_var.get() - 1)
                update_display()
                
        def next_step():
            if step_var.get() < len(steps) - 1:
                step_var.set(step_var.get() + 1)
                update_display()
                
        
        def play_animation():
            current = step_var.get()
            if current < len(steps) - 1:
                step_var.set(current + 1)
                update_display()
                anim_win.after(2000, play_animation)
        
        nav_frame = ctk.CTkFrame(bottom_frame)
        nav_frame.pack(side="bottom", fill="x", pady=10)
        
        prev_btn = ctk.CTkButton(nav_frame, text="< Prev", command=prev_step)
        prev_btn.pack(side="left", padx=10)
        
        next_btn = ctk.CTkButton(nav_frame, text="Next >", command=next_step)
        next_btn.pack(side="right", padx=10)
        
        play_btn = ctk.CTkButton(nav_frame, text="▶ Play", command=play_animation)
        play_btn.pack(side="bottom", padx=10, pady=5)
        
        update_display()
        
    except Exception as e:
        messagebox.showerror("Animation Error", f"Error creating optimization animation: {str(e)}")

def visualize_graph(cfg, filename="cfg.png"):
    try:
        dot_str = "digraph CFG {\n"
        dot_str += "  rankdir=TB;\n"
        dot_str += "  node [shape=box, style=filled, fontname=\"Consolas\", fontsize=10];\n"
        
        for node in sorted(cfg.nodes):
            instrs = cfg.nodes[node].get("instrs", [])
            label_lines = [instr.getText() if hasattr(instr, "getText") else str(instr) 
                        for instr in instrs]
            label = f"BB{node}\\n" + "\\n".join(label_lines)
            
            
            highlight = cfg.nodes[node].get('highlight', False)
            fillcolor = "#ffcc99" if highlight else "#e3f2fd"
            
            dot_str += f'  node{node} [label="{label}", fillcolor="{fillcolor}"];\n'
            
        for src, dst in cfg.edges():
            dot_str += f'  node{src} -> node{dst};\n'
            
        dot_str += "}\n"
        
        src = Source(dot_str, filename=os.path.splitext(filename)[0], format="png")
        src.render(cleanup=True)
        return True
    except Exception as e:
        print(f"Error visualizing CFG: {e}")
        return False

def generate_dot(tree, parser):
    node_lines = []
    edges = []
    node_counter = 0

    def visit(node):
        nonlocal node_counter
        current_id = node_counter
        node_counter += 1

        label = ""
        if hasattr(node, "getRuleIndex"):
            rule_index = node.getRuleIndex()
            if rule_index >= 0 and rule_index < len(parser.ruleNames):
                label = parser.ruleNames[rule_index]
        if not label:
            label = node.getText()
        label = label.replace('"', "'")
        node_lines.append(f'  node{current_id} [label="{label}"];')
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            child_id = visit(child)
            edges.append(f'  node{current_id} -> node{child_id};')
        return current_id

    visit(tree)
    dot_str = "digraph ParseTree {\n" + "\n".join(node_lines + edges) + "\n}"
    return dot_str

def lex_input():
    input_text = editor.get("1.0", tk.END)
    in_stream = InputStream(input_text)
    lexer = WhileLexer(in_stream)
    
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    result = "Lexer Output:\n"
    for token in token_stream.getTokens(0, len(token_stream.tokens) - 1):
        if token.type == Token.EOF:
            continue
        token_type = (WhileLexer.symbolicNames[token.type-2]
                      if 0 <= token.type-2 < len(WhileLexer.symbolicNames)
                      else str(token.type))
        result += f"{token.text}  ({token_type})\n"
    
    output.configure(state='normal')
    output.delete("1.0", tk.END)
    output.insert("1.0", result)
    output.configure(state='disabled')

def parse_input():
    input_text = editor.get("1.0", tk.END)
    in_stream = InputStream(input_text)
    lexer = WhileLexer(in_stream)
    token_stream = CommonTokenStream(lexer)
    parser = WhileParser(token_stream)
    
    tree = parser.s()
    
    result = "Parse Tree (Textual):\n" + tree.toStringTree(recog=parser) + "\n\n"
    
    dot_code = generate_dot(tree, parser)
    src = Source(dot_code, filename="parsetree", format="png")
    png_path = src.render()
    show_parse_tree_image(png_path)
    
    output.configure(state='normal')
    output.delete("1.0", tk.END)
    output.insert("1.0", result)
    output.configure(state='disabled')

def show_parse_tree_image(png_path):
    tree_window = ctk.CTkToplevel(root)
    tree_window.transient(root)
    tree_window.lift()
    tree_window.attributes("-topmost", True)
    tree_window.after_idle(lambda: tree_window.attributes("-topmost", False))
    tree_window.title("Graphical Parse Tree")

    frame = CTkFrame(tree_window, corner_radius=10)
    frame.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(frame)
    scrollbar_x = CTkScrollbar(frame, orientation="horizontal", command=canvas.xview)
    scrollbar_y = CTkScrollbar(frame, orientation="vertical", command=canvas.yview)
    canvas.configure(xscrollcommand=scrollbar_x.set, yscrollcommand=scrollbar_y.set)

    scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
    scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    orig_img = Image.open(png_path)
    photo = ImageTk.PhotoImage(orig_img)
    img_id = canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.image = photo

    canvas.config(scrollregion=(0, 0, orig_img.width, orig_img.height))

    def _on_resize(event):
        w, h = event.width, event.height
        if w < 2 or h < 2:
            return
        resized = orig_img.resize((w, h), Image.LANCZOS)
        new_photo = ImageTk.PhotoImage(resized)
        canvas.itemconfig(img_id, image=new_photo)
        canvas.image = new_photo
        canvas.config(scrollregion=(0, 0, w, h))

    canvas.bind("<Configure>", _on_resize)

    tree_window.geometry("800x600")
    tree_window.resizable(True, True)

def emit_code():
    input_text = editor.get("1.0", tk.END)
    in_stream = InputStream(input_text)
    ir_buf = StringIO()
    irgen(in_stream, ir_buf)
    ir_code = ir_buf.getvalue()
    if optimize_ir:
        ir_code = optimize_ir_code(ir_code)
    output.configure(state='normal')
    output.delete("1.0", tk.END)
    label = "Optimized IR Code Output:" if optimize_ir else "IR Code Output:"
    output.insert("1.0", f"{label}\n{ir_code}")
    output.configure(state='disabled')

def emit_c():
    input_text = editor.get("1.0", tk.END)
    in_stream = InputStream(input_text)
    lexer = WhileLexer(in_stream)
    stream = CommonTokenStream(lexer)
    parser = WhileParser(stream)
    tree = parser.s()
    cgen = CGen()
    c_code = cgen.emit(tree)
    output.configure(state='normal')
    output.delete("1.0", tk.END)
    output.insert("1.0", c_code)
    output.configure(state='disabled')

def emit_py():
    input_text = editor.get("1.0", tk.END)
    in_stream = InputStream(input_text)
    lexer = WhileLexer(in_stream)
    stream = CommonTokenStream(lexer)
    parser = WhileParser(stream)
    tree = parser.s()
    pygen = PythonGen()
    py_code = pygen.emit(tree)
    output.configure(state='normal')
    output.delete("1.0", tk.END)
    output.insert("1.0", py_code)
    output.configure(state='disabled')

def show_cfg():
    global last_cfg
    try:
        input_text = editor.get("1.0", tk.END)
        in_stream = InputStream(input_text)
        ir_buf = StringIO()
        irgen(in_stream, ir_buf)
        ir_code = ir_buf.getvalue()
        
        if optimize_ir:
            if not last_cfg:
                optimize_ir_code(ir_code)
            cfg = last_cfg
        else:
            lexer = SimpleIRLexer(InputStream(ir_code))
            stream = CommonTokenStream(lexer)
            parser = SimpleIRParser(stream)
            tree = parser.unit()
            walker = ParseTreeWalker()
            irl = IRList()
            walker.walk(irl, tree)
            instrs = irl.instr
            cfg = build_cfg(instrs)
        
        cfg_png = "cfg.png"
        if not visualize_graph(cfg, filename=cfg_png):
            raise Exception("Failed to visualize CFG")
        
        window_title = "CFG (Optimized IR)" if optimize_ir else "CFG (Original IR)"
        show_parse_tree_image(cfg_png)
        
        for win in root.winfo_children():
            if isinstance(win, ctk.CTkToplevel) and win.title() == "Graphical Parse Tree":
                win.title(window_title)
                break
                
        editor.focus_set()
        
    except Exception as e:
        output.configure(state='normal')
        output.delete("1.0", tk.END)
        output.insert("1.0", f"Error generating CFG: {str(e)}")
        output.configure(state='disabled')
        editor.focus_set()

def show_help():
    help_text = (
    "While Language Guide:\n\n"
    "Statements:\n"
    "----------\n"
    "1. Assignment:\n"
    "   - Syntax: ID := a\n"
    "   - Description: Assign an arithmetic expression to a variable.\n"
    "   - Example: x := 5 + 3\n\n"
    "2. Skip:\n"
    "   - Syntax: skip\n"
    "   - Description: Do nothing (a no-operation).\n"
    "   - Example: skip\n\n"
    "3. Compound Statements:\n"
    "   - Syntax: begin s; s; ...; s end\n"
    "   - Description: Group multiple statements together.\n"
    "   - Example:\n"
    "         begin\n"
    "             x := 5;\n"
    "             y := x + 2;\n"
    "         end\n\n"
    "4. Conditional (If) Statements:\n"
    "   - Syntax: if b then s else s\n"
    "   - Description: Execute one statement if a boolean expression is true; otherwise, execute the other.\n"
    "   - Example: if x < 10 then x := x + 1 else x := x - 1\n\n"
    "5. Loop (While) Statements:\n"
    "   - Syntax: while b do s\n"
    "   - Description: Repeat a statement as long as a boolean condition remains true.\n"
    "   - Example: while x < 10 do x := x + 1\n\n"
    "Expressions:\n"
    "------------\n"
    "Boolean Expressions (b):\n"
    "   - Literals: true, false\n"
    "   - Negation: not b\n"
    "   - Conjunction: b and b\n"
    "   - Disjunction: b or b\n"
    "   - Relational: a ROP a  (e.g., x < y, x = y, etc.)\n"
    "   - Grouping: ( b )\n"
    "   - Example: not (x >= 10) and true\n\n"
    "Arithmetic Expressions (a):\n"
    "   - Literals: ID (variable), NUM (number)\n"
    "   - Operations: a AOP a (using +, -, *, /)\n"
    "   - Grouping: ( a )\n"
    "   - Example: (x + 3) * (y - 2)\n\n"
    "Operators:\n"
    "----------\n"
    "1. Relational: <, <=, =, >, >=\n"
    "2. Arithmetic: +, -, *, /\n\n"
    "Grammar Overview:\n"
    "-----------------\n"
    "A valid statement (s) in the While language can be one of the following:\n"
    "  s:\n"
    "     ID := a                (Assignment)\n"
    "   | skip                   (Skip)\n"
    "   | begin s; s; ...; s end  (Compound Statement)\n"
    "   | if b then s else s     (Conditional)\n"
    "   | while b do s           (Loop)\n\n"
    "Boolean expressions (b) include:\n"
    "  true | false | not b | b and b | b or b | a ROP a | ( b )\n\n"
    "Arithmetic expressions (a) include:\n"
    "  ID | NUM | a AOP a | ( a )\n\n"
    "Operators:\n"
    "----------\n"
    "1. Relational: <, <=, =, >, >=\n"
    "2. Arithmetic: +, -, *, /\n\n"    
)


    def show_grammar():
        grammar_text = (
            "While Language Grammar:\n\n"
            "s -> ID := a\n"
            "   | skip\n"
            "   | begin s; s; ...; s end\n"
            "   | if b then s else s\n"
            "   | while b do s\n\n"
            "a -> ID\n"
            "   | NUM\n"
            "   | a AOP a\n\n"
            "b -> true\n"
            "   | false\n"
            "   | not b\n"
            "   | b and b\n"
            "   | b or b\n"
            "   | a ROP a\n\n"
            "AOP -> + | - | * | /\n"
            "ROP -> < | <= | = | > | >=\n"
        )
        grammar_win = ctk.CTkToplevel(root)
        grammar_win.title("While Language Grammar")
        grammar_win.transient(root); grammar_win.lift()
        grammar_win.attributes("-topmost", True)
        grammar_win.after_idle(lambda: grammar_win.attributes("-topmost", False))

        frame = ctk.CTkFrame(grammar_win, corner_radius=8)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        box = CTkTextbox(frame, font=("Consolas",12),
                         fg_color=frame.cget("fg_color"))
        box.pack(fill="both", expand=True, padx=5, pady=5)
        box.insert("0.0", grammar_text)
        box.configure(state="disabled")

        CTkButton(frame, text="Close", 
                  command=grammar_win.destroy).pack(pady=(5,10))

    help_win = ctk.CTkToplevel(root)
    help_win.title("While Language Help")
    help_win.transient(root); help_win.lift()
    help_win.attributes("-topmost", True)
    help_win.after_idle(lambda: help_win.attributes("-topmost", False))

    frame = ctk.CTkFrame(help_win, corner_radius=8)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    box = CTkTextbox(frame, font=("Consolas",12),
                     fg_color=frame.cget("fg_color"))
    box.pack(fill="both", expand=True, padx=5, pady=5)
    box.insert("0.0", help_text)
    box.configure(state="disabled")

    CTkButton(frame, text="Close", 
              command=help_win.destroy).pack(pady=(5,10))

root = ctk.CTk()
root.title("While Language IDE")
root.geometry("1000x700")

main_frame = ctk.CTkFrame(root, corner_radius=15)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

sidebar = ctk.CTkFrame(main_frame, corner_radius=10, width=200)
sidebar.pack(side="left", fill="y", padx=(0,10), pady=10)

ctk.CTkLabel(sidebar, text="🌀 WhileLang", font=CTkFont(size=24, weight="bold"))\
    .pack(pady=(20,40))

optimize_button = None
for txt, cmd in [
    ("Lex",          lex_input),
    ("Parse",        parse_input),
    ("Emit IR",      emit_code),
    ("Toggle Opt",   toggle_optimization),
    ("Show CFG",     show_cfg),
    ("Animate Opt",  show_optimization_animation),
    ("Generate C",   emit_c),
    ("Generate Py",  emit_py),    
    ("Help",         show_help),
]:
    btn = ctk.CTkButton(sidebar, text=txt, command=cmd,
                        corner_radius=8, height=40,
                        fg_color=sidebar.cget("fg_color"),
                        hover_color="#444444")
    btn.pack(fill="x", padx=20, pady=5)
    if txt == "Toggle Opt":
        optimize_button = btn
optimize_button.configure(fg_color="#AA0000", hover_color="#CC0000")

editor_frame = ctk.CTkFrame(main_frame, corner_radius=10)
editor_frame.pack(side="left", fill="both", expand=True, padx=(0,10), pady=10)
ctk.CTkLabel(editor_frame, text="Input Code:", font=CTkFont(size=14, weight="bold"))\
    .pack(anchor="nw", pady=(0,5))
editor = CTkTextbox(editor_frame, corner_radius=10, font=("Consolas", 16))
editor.pack(fill="both", expand=True)

output_frame = ctk.CTkFrame(main_frame, corner_radius=10)
output_frame.pack(side="right", fill="both", expand=True, padx=(10,0), pady=10)
ctk.CTkLabel(output_frame, text="Output:", font=CTkFont(size=14, weight="bold"))\
    .pack(anchor="nw", pady=(0,5))
output = CTkTextbox(output_frame, corner_radius=10, font=("Consolas", 16))
output.pack(fill="both", expand=True)
output.configure(state="disabled")

root.mainloop()