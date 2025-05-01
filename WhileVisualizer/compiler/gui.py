import tkinter as tk               
import customtkinter as ctk
from customtkinter import CTkFont, CTkTextbox, CTkFrame, CTkLabel, CTkButton, CTkScrollbar
from antlr4 import InputStream, CommonTokenStream, Token, ParseTreeWalker
from PIL import Image, ImageTk
import time
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
from graphviz import Source


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Global variables
optimize_ir = False
last_cfg = None
optimization_steps = []

# Function to toggle optimization on/off
def toggle_optimization():
    global optimize_ir, optimize_button
    
    # If optimization is currently off, turn it on
    if optimize_ir == False:
        optimize_ir = True
        optimize_button.configure(text="Optimization: ON", fg_color="#00AA00", hover_color="#00CC00")
    # If optimization is currently on, turn it off
    else:
        optimize_ir = False
        optimize_button.configure(text="Optimization: OFF", fg_color="#AA0000", hover_color="#CC0000")

# Function to optimize IR code
def optimize_ir_code(ir_code):
    global last_cfg
    
    # Split the code into lines
    lines = ir_code.strip().split('\n')
    
    # Check if there's any code
    if len(lines) == 0:
        return ir_code

    # Initialize variables
    header = None
    footer = []
    body = []
    
    # Process each line
    for line in lines:
        # If line starts with "function", it's the header
        if line.startswith("function "):
            header = line
        else:
            # If line is footer (return or end function)
            if line.startswith("return ") or line.startswith("end function"):
                footer.append(line)
            else:
                # Check if line is a comment
                is_comment = False
                if len(line.strip()) > 0:
                    if line.strip()[0] == "#":
                        is_comment = True
                
                # If not a comment, add to body
                if is_comment == False:
                    body.append(line)

    # Default header if none found
    if header == None:
        header = "function main"

    # Rebuild the full IR code
    full_ir = header + "\n"
    
    
    for b_line in body:
        full_ir = full_ir + b_line + "\n"
    
    # Add footer lines
    for f_line in footer:
        full_ir = full_ir + f_line + "\n"
    
    # Parse the IR code
    lexer = SimpleIRLexer(InputStream(full_ir))
    stream = CommonTokenStream(lexer)
    parser = SimpleIRParser(stream)
    tree = parser.unit()

    
    if parser.getNumberOfSyntaxErrors() > 0:
        optimized_lines = body
    else:
        # Build CFG
        walker = ParseTreeWalker()
        irl = IRList()
        walker.walk(irl, tree)
        instrs = irl.instr
        cfg = build_cfg(instrs)
        cfg = dataflow_analysis(cfg)
        last_cfg = cfg
        optimized_ir = reconstruct_ir(cfg)
        
        # Extract non-empty lines
        optimized_lines = []
        split_lines = optimized_ir.strip().split('\n')
        for l in split_lines:
            if len(l.strip()) > 0:
                optimized_lines.append(l)
    
    # Rebuild result
    result = []
    result.append(header)
    
    for line in optimized_lines:
        result.append(line)
    
    for line in footer:
        result.append(line)
    
    # Join result 
    final_result = ""
    for i in range(len(result)):
        if i > 0:
            final_result = final_result + "\n"
        final_result = final_result + result[i]
    
    return final_result

#instruction class
class SimpleInstruction:
    def __init__(self, text):
        self.text = text
        
    def getText(self):
        return self.text

# Find nodes containing a variable
def find_nodes_with_var(cfg, var):
    nodes = []
    
    for node in cfg.nodes:
        for instr in cfg.nodes[node].get("instrs", []):
            if var in instr.getText():
                nodes.append(node)
                break
                
    return nodes

#optimization animation
def show_optimization_animation():
    # Get the input code
    input_text = editor.get("1.0", tk.END)
    in_stream = InputStream(input_text)
    
    # Generate IR code
    ir_buf = StringIO()
    irgen(in_stream, ir_buf)
    ir_code = ir_buf.getvalue()
    
   
    steps = []
    
    # Parse IR code
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
    
    # Build initial CFG
    cfg = build_cfg(text_instrs)
    
    
    step1 = {}
    step1['cfg'] = cfg
    step1['description'] = "Initial CFG before optimization"
    step1['constants'] = {}
    steps.append(step1)
    
    # Find constants
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
    
    # If constants found create step
    if len(constants) > 0:
        cfg2 = nx.DiGraph()
        
       
        for node in cfg.nodes:
            cfg2.add_node(node, instrs=cfg.nodes[node].get("instrs", []))
            
        
        for edge in cfg.edges:
            cfg2.add_edge(edge[0], edge[1])
            
        # Find nodes with variables
        highlight_nodes = []
        for var in constants:
            nodes_with_var = find_nodes_with_var(cfg, var)
            for node in nodes_with_var:
                if node not in highlight_nodes:
                    highlight_nodes.append(node)
                
       
        step2 = {}
        step2['cfg'] = cfg2
        step2['description'] = f"Constants identified: {constants}"
        step2['constants'] = dict(constants)
        step2['highlight_nodes'] = highlight_nodes
        steps.append(step2)
        
        # Process each constant
        for var in constants:
            val = constants[var]
            
            # Find nodes affected by this variable
            affected_nodes = find_nodes_with_var(cfg, var)
            
            # If nodes found, create step
            if len(affected_nodes) > 0:
                const_cfg = nx.DiGraph()
                
                # Copy nodes with instructions
                for node in cfg.nodes:
                    instrs_copy = []
                    for i in cfg.nodes[node].get("instrs", []):
                        # Keep original text for non-affected nodes
                        if node not in affected_nodes:
                            instrs_copy.append(SimpleInstruction(i.getText()))
                        else:
                            
                            orig_text = i.getText()
                            
                            pattern = r'\b' + re.escape(var) + r'\b'
                            
                            modified_text = re.sub(pattern, str(val), orig_text)
                            instrs_copy.append(SimpleInstruction(modified_text))
                    
                    const_cfg.add_node(node, instrs=instrs_copy)
                    
                # Copy edges
                for edge in cfg.edges:
                    const_cfg.add_edge(edge[0], edge[1])
                    
                # Create step
                step = {}
                step['cfg'] = const_cfg
                step['description'] = f"Propagating constant: {var} = {val}"
                step['constants'] = dict(constants)
                step['highlight_nodes'] = affected_nodes
                steps.append(step)
        
        # Add dead code elimination step if applicable
        eliminated_nodes = []
        final_cfg = nx.DiGraph()
        
        # Copy nodes with potentially eliminated instructions
        for node in cfg.nodes:
            instrs_copy = []
            eliminated_in_node = False
            
            for i in cfg.nodes[node].get("instrs", []):
                orig_text = i.getText()
                
                # Check if this is an if statement with a constant condition
                if "if " in orig_text:
                    
                    condition_text = orig_text
                    for cvar, cval in constants.items():
                        pattern = r'\b' + re.escape(cvar) + r'\b'
                        condition_text = re.sub(pattern, str(cval), condition_text)
                    
                    # If condition now has only constants, it can be evaluated
                    if sum(1 for cv in constants if cv in condition_text) == 0:
                        # Mark as eliminated
                        eliminated_in_node = True
                        eliminated_nodes.append(node)
                    
                # Keep non-eliminated instructions
                if not eliminated_in_node:
                   
                    modified_text = orig_text
                    for cvar, cval in constants.items():
                        pattern = r'\b' + re.escape(cvar) + r'\b'
                        modified_text = re.sub(pattern, str(cval), modified_text)
                    instrs_copy.append(SimpleInstruction(modified_text))
            
            final_cfg.add_node(node, instrs=instrs_copy)
        
        
        for edge in cfg.edges:
            final_cfg.add_edge(edge[0], edge[1])
        
        # Create final step if we eliminated code
        if eliminated_nodes:
            step_final = {}
            step_final['cfg'] = final_cfg
            step_final['description'] = "Final optimized code with dead code eliminated"
            step_final['constants'] = dict(constants)
            step_final['highlight_nodes'] = eliminated_nodes
            steps.append(step_final)
    
   
    if len(steps) <= 1:
        messagebox.showinfo("Optimization Animation", "No optimization steps to show!")
        return
        
    # Create animation window
    anim_win = ctk.CTkToplevel(root)
    anim_win.title("Optimization Animation")
    anim_win.geometry("800x700")
    anim_win.transient(root)
    anim_win.lift()
    
    
    top_frame = ctk.CTkFrame(anim_win)
    top_frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    bottom_frame = ctk.CTkFrame(anim_win)
    bottom_frame.pack(fill="x", padx=10, pady=10)
    
    # Create labels
    desc_label = ctk.CTkLabel(top_frame, text="", font=("Consolas", 14))
    desc_label.pack(pady=10)
    
    img_label = tk.Label(top_frame)
    img_label.pack(fill="both", expand=True, padx=10, pady=10)
    
    step_var = tk.IntVar(value=0)
    
    # Function to update display
    def update_display(event=None):
        step = step_var.get()
        
        if step >= 0 and step < len(steps):
            # Update description
            desc_label.configure(text=steps[step]['description'])
            
            
            cfg = steps[step]['cfg']
            
           
            highlight_nodes = []
            if 'highlight_nodes' in steps[step]:
                highlight_nodes = steps[step]['highlight_nodes']
            
            # Set highlighting
            for node in cfg.nodes:
                if node in highlight_nodes:
                    cfg.nodes[node]['highlight'] = True
                else:
                    cfg.nodes[node]['highlight'] = False
            
            # Create image
            step_img = "step_" + str(step) + ".png"
            visualize_graph(cfg, filename=step_img)
            
            # Display image
            img = Image.open(step_img)
            img = img.resize((700, 500), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            img_label.configure(image=photo)
            img_label.image = photo
            
            
            step_text = "Step " + str(step+1) + "/" + str(len(steps))
            step_counter.configure(text=step_text)
    
    # Create slider
    slider = ctk.CTkSlider(
        bottom_frame,
        from_=0,
        to=len(steps)-1,
        number_of_steps=len(steps)-1,
        command=update_display,
        variable=step_var
    )
    slider.pack(fill="x", padx=20, pady=10, side="left", expand=True)
    
    # Create step counter
    step_counter = ctk.CTkLabel(bottom_frame, text=f"Step 1/{len(steps)}")
    step_counter.pack(side="right", padx=10)
    
    # Functions for navigation
    def prev_step():
        if step_var.get() > 0:
            step_var.set(step_var.get() - 1)
            update_display()
            
    def next_step():
        if step_var.get() < len(steps) - 1:
            step_var.set(step_var.get() + 1)
            update_display()
    
    # Function to play animation        
    def play_animation():
        current = step_var.get()
        if current < len(steps) - 1:
            step_var.set(current + 1)
            update_display()
            anim_win.after(2000, play_animation)
    
    # Create navigation frame
    nav_frame = ctk.CTkFrame(bottom_frame)
    nav_frame.pack(side="bottom", fill="x", pady=10)
    
    # Create navigation buttons
    prev_btn = ctk.CTkButton(nav_frame, text="< Prev", command=prev_step)
    prev_btn.pack(side="left", padx=10)
    
    next_btn = ctk.CTkButton(nav_frame, text="Next >", command=next_step)
    next_btn.pack(side="right", padx=10)
    
    play_btn = ctk.CTkButton(nav_frame, text="▶ Play", command=play_animation)
    play_btn.pack(side="bottom", padx=10, pady=5)
    
    
    update_display()

# Visualize CFG
def visualize_graph(cfg, filename="cfg.png"):
    # Create DOT string for graph visualization
    dot_str = "digraph CFG {\n"
    dot_str = dot_str + "  rankdir=TB;\n"
    dot_str = dot_str + "  node [shape=box, style=filled, fontname=\"Consolas\", fontsize=10];\n"
    
    # Add nodes
    for node in sorted(cfg.nodes):
        
        instrs = cfg.nodes[node].get("instrs", [])
        
       
        label_lines = []
        for instr in instrs:
            if hasattr(instr, "getText"):
                label_lines.append(instr.getText())
            else:
                label_lines.append(str(instr))
                
        # Join lines
        label = f"BB{node}\\n" + "\\n".join(label_lines)
        
       
        highlight = False
        if 'highlight' in cfg.nodes[node]:
            highlight = cfg.nodes[node]['highlight']
            
        fillcolor = "#ffcc99" if highlight else "#e3f2fd"
        
        # Add node to DOT
        dot_str = dot_str + f'  node{node} [label="{label}", fillcolor="{fillcolor}"];\n'
        
   
    for edge in cfg.edges():
        src = edge[0]
        dst = edge[1]
        dot_str = dot_str + f'  node{src} -> node{dst};\n'
        
    dot_str = dot_str + "}\n"
    
    # Render the graph
    src = Source(dot_str, filename=os.path.splitext(filename)[0], format="png")
    src.render(cleanup=True)
    return True

# Generate DOT for parse tree visualization
def generate_dot(tree, parser):
    node_lines = []
    edges = []
    node_counter = 0

    def visit(node):
        nonlocal node_counter
        current_id = node_counter
        node_counter = node_counter + 1

        # Get label for node
        label = ""
        
        # If it's a rule node get rule name
        if hasattr(node, "getRuleIndex"):
            rule_index = node.getRuleIndex()
            if rule_index >= 0 and rule_index < len(parser.ruleNames):
                label = parser.ruleNames[rule_index]
                
        # If no label yet, use node text
        if label == "":
            label = node.getText()
            
        # Escape quotes
        label = label.replace('"', "'")
        
       
        node_lines.append(f'  node{current_id} [label="{label}"];')
        
        # Process children
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            child_id = visit(child)
            edges.append(f'  node{current_id} -> node{child_id};')
            
        return current_id

    
    visit(tree)
    
    # Create DOT string
    dot_str = "digraph ParseTree {\n" + "\n".join(node_lines + edges) + "\n}"
    return dot_str

# Handle lexer operation
def lex_input():
    # Get input text
    input_text = editor.get("1.0", tk.END)
    in_stream = InputStream(input_text)
    
  
    lexer = WhileLexer(in_stream)
    
   
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    # Create result
    result = "Lexer Output:\n"
    for i in range(len(token_stream.tokens) - 1):
        token = token_stream.tokens[i]
        if token.type == Token.EOF:
            continue
        
        # Get token type name
        token_type = ""
        if token.type - 2 >= 0 and token.type - 2 < len(WhileLexer.symbolicNames):
            token_type = WhileLexer.symbolicNames[token.type-2]
        else:
            token_type = str(token.type)
            
        # Add token to result
        result = result + f"{token.text}  ({token_type})\n"
    
    # Update output
    output.configure(state='normal')
    output.delete("1.0", tk.END)
    output.insert("1.0", result)
    output.configure(state='disabled')

# Handle parser operation
def parse_input():
    
    input_text = editor.get("1.0", tk.END)
    in_stream = InputStream(input_text)
    
   
    lexer = WhileLexer(in_stream)
    token_stream = CommonTokenStream(lexer)
    parser = WhileParser(token_stream)
    
 
    tree = parser.s()
    
   
    result = "Parse Tree (Textual):\n" + tree.toStringTree(recog=parser) + "\n\n"
    
    # Create graphical result
    dot_code = generate_dot(tree, parser)
    src = Source(dot_code, filename="parsetree", format="png")
    png_path = src.render()
    show_parse_tree_image(png_path)
    
    # Update output
    output.configure(state='normal')
    output.delete("1.0", tk.END)
    output.insert("1.0", result)
    output.configure(state='disabled')

# Show parse tree image
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
        w = event.width
        h = event.height
        
      
        if w < 2 or h < 2:
            return
            
    
        resized = orig_img.resize((w, h), Image.LANCZOS)
        new_photo = ImageTk.PhotoImage(resized)
        canvas.itemconfig(img_id, image=new_photo)
        canvas.image = new_photo
        canvas.config(scrollregion=(0, 0, w, h))

    # Bind resize event
    canvas.bind("<Configure>", _on_resize)

 
    tree_window.geometry("800x600")
    tree_window.resizable(True, True)

# Generate IR code
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
    
    # Set label based on optimization
    label = ""
    if optimize_ir:
        label = "Optimized IR Code Output:"
    else:
        label = "IR Code Output:"
        
    output.insert("1.0", f"{label}\n{ir_code}")
    output.configure(state='disabled')

# Generate C code
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

# Generate Python code
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

# Show CFG
def show_cfg():
    global last_cfg
    

    input_text = editor.get("1.0", tk.END)
    in_stream = InputStream(input_text)
    
    # Generate IR
    ir_buf = StringIO()
    irgen(in_stream, ir_buf)
    ir_code = ir_buf.getvalue()
    
    # Get CFG based on optimization setting
    if optimize_ir:
       
        if last_cfg == None:
            optimize_ir_code(ir_code)
        cfg = last_cfg
    else:
        # Generate CFG from IR
        lexer = SimpleIRLexer(InputStream(ir_code))
        stream = CommonTokenStream(lexer)
        parser = SimpleIRParser(stream)
        tree = parser.unit()
        walker = ParseTreeWalker()
        irl = IRList()
        walker.walk(irl, tree)
        instrs = irl.instr
        cfg = build_cfg(instrs)
    
    # Generate CFG image
    cfg_png = "cfg.png"
    visualize_graph(cfg, filename=cfg_png)
    
    
    window_title = ""
    if optimize_ir:
        window_title = "CFG (Optimized IR)"
    else:
        window_title = "CFG (Original IR)"
        
    # Show image
    show_parse_tree_image(cfg_png)
    
    
    for win in root.winfo_children():
        if isinstance(win, ctk.CTkToplevel) and win.title() == "Graphical Parse Tree":
            win.title(window_title)
            break
            
   
    editor.focus_set()

# Show help
def show_help():
    help_text = (
        "While Language Guide:\n\n"
        "Statements:\n"
        "----------\n"
        "1. Assignment:\n"
        "   - Syntax: ID := a\n"
        "   - Example: x := 5 + 3\n\n"
        "2. Skip:\n"
        "   - Syntax: skip\n"
        "   - Example: skip\n\n"
        "3. Compound Statements:\n"
        "   - Syntax: begin s; s; ...; s end\n"
        "   - Example:\n"
        "         begin\n"
        "             x := 5;\n"
        "             y := x + 2;\n"
        "         end\n\n"
        "4. Conditional (If) Statements:\n"
        "   - Syntax: if b then s else s\n"
        "   - Example: if x < 10 then x := x + 1 else x := x - 1\n\n"
        "5. Loop (While) Statements:\n"
        "   - Syntax: while b do s\n"
        "   - Example: while x < 10 do x := x + 1\n\n"
        "Expressions:\n"
        "------------\n"
        "Boolean (b): true, false, not b, b and b, b or b, a ROP a, ( b )\n"
        "Arithmetic (a): ID, NUM, a AOP a, ( a )\n\n"
        "Operators:\n"
        "----------\n"
        "Relational: <, <=, =, >, >=\n"
        "Arithmetic: +, -, *, /\n"
    )

    # Create help window
    help_win = ctk.CTkToplevel(root)
    help_win.title("While Language Help")
    help_win.transient(root)
    help_win.lift()
    help_win.attributes("-topmost", True)
    help_win.after_idle(lambda: help_win.attributes("-topmost", False))


    frame = ctk.CTkFrame(help_win, corner_radius=8)
    frame.pack(fill="both", expand=True, padx=10, pady=10)


    box = CTkTextbox(frame, font=("Consolas",12), fg_color=frame.cget("fg_color"))
    box.pack(fill="both", expand=True, padx=5, pady=5)
    box.insert("0.0", help_text)
    box.configure(state="disabled")

  
    CTkButton(frame, text="Close", command=help_win.destroy).pack(pady=(5,10))

# Create main window
root = ctk.CTk()
root.title("While Language IDE")
root.geometry("1000x700")


main_frame = ctk.CTkFrame(root, corner_radius=15)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)


sidebar = ctk.CTkFrame(main_frame, corner_radius=10, width=200)
sidebar.pack(side="left", fill="y", padx=(0,10), pady=10)

# Add title to sidebar
ctk.CTkLabel(sidebar, text="🌀 WhileLang", font=CTkFont(size=24, weight="bold"))\
    .pack(pady=(20,40))

# Create buttons
optimize_button = None


button_texts = ["Lex", "Parse", "Emit IR", "Toggle Opt", "Show CFG", 
               "Animate Opt", "Generate C", "Generate Py", "Help"]
               
button_commands = [lex_input, parse_input, emit_code, toggle_optimization,
                  show_cfg, show_optimization_animation, emit_c, emit_py,
                  show_help]


for i in range(len(button_texts)):
    btn = ctk.CTkButton(sidebar, text=button_texts[i], command=button_commands[i],
                    corner_radius=8, height=40,
                    fg_color=sidebar.cget("fg_color"),
                    hover_color="#444444")
    btn.pack(fill="x", padx=20, pady=5)
    
  
    if button_texts[i] == "Toggle Opt":
        optimize_button = btn

# Configure optimize button
optimize_button.configure(fg_color="#AA0000", hover_color="#CC0000")


editor_frame = ctk.CTkFrame(main_frame, corner_radius=10)
editor_frame.pack(side="left", fill="both", expand=True, padx=(0,10), pady=10)


ctk.CTkLabel(editor_frame, text="Input Code:", font=CTkFont(size=14, weight="bold"))\
    .pack(anchor="nw", pady=(0,5))
    

editor = CTkTextbox(editor_frame, corner_radius=10, font=("Consolas", 16))
editor.pack(fill="both", expand=True)

# Create output frame
output_frame = ctk.CTkFrame(main_frame, corner_radius=10)
output_frame.pack(side="right", fill="both", expand=True, padx=(10,0), pady=10)

# Add output label
ctk.CTkLabel(output_frame, text="Output:", font=CTkFont(size=14, weight="bold"))\
    .pack(anchor="nw", pady=(0,5))

output = CTkTextbox(output_frame, corner_radius=10, font=("Consolas", 16))
output.pack(fill="both", expand=True)
output.configure(state="disabled")

root.mainloop()