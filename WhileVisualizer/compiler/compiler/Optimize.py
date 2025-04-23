#!/usr/bin/env python3
import os
import sys
import itertools
from collections import defaultdict, deque
from antlr4 import *
from simpleir.SimpleIRLexer import SimpleIRLexer
from simpleir.SimpleIRParser import SimpleIRParser
from simpleir.SimpleIRListener import SimpleIRListener
import logging
logging.basicConfig(level=logging.DEBUG)
import networkx as nx
from graphviz import Source  # Import the graphviz package
import re  # Add this import at the top with other imports

# ---------------------------------------------------------------------------
# IR Listener: collects all IR instructions from the parse tree.
# ---------------------------------------------------------------------------
class IRList(SimpleIRListener):
    def __init__(self):
        self.instr = []
    def enterOperation(self, ctx: SimpleIRParser.OperationContext):
        self.instr.append(ctx)
    def enterAssign(self, ctx: SimpleIRParser.AssignContext):
        self.instr.append(ctx)
    def enterDereference(self, ctx: SimpleIRParser.DereferenceContext):
        self.instr.append(ctx)
    def enterReference(self, ctx: SimpleIRParser.ReferenceContext):
        self.instr.append(ctx)
    def enterAssignDereference(self, ctx: SimpleIRParser.AssignDereferenceContext):
        self.instr.append(ctx)
    def enterCall(self, ctx: SimpleIRParser.CallContext):
        self.instr.append(ctx)
    def enterLabel(self, ctx: SimpleIRParser.LabelContext):
        self.instr.append(ctx)
    def enterGotoStatement(self, ctx: SimpleIRParser.GotoStatementContext):
        self.instr.append(ctx)
    def enterIfGoto(self, ctx: SimpleIRParser.IfGotoContext):
        self.instr.append(ctx)

# ---------------------------------------------------------------------------
# CFG Graph Helpers (visual and textual)
# ---------------------------------------------------------------------------
def cfg_to_dot(cfg):
    """Generate a DOT string representation of the CFG with IR in nodes."""
    lines = [
        "digraph CFG {",
        "  rankdir=TB;",
        "  node [shape=box, style=filled, fillcolor=\"#e3f2fd\", fontname=\"Consolas\", fontsize=10];"
    ]
    for node in sorted(cfg.nodes):
        instrs = cfg.nodes[node].get("instrs", [])
        label_lines = [instr.getText().replace('\\', '\\\\').replace('"', '\\"') for instr in instrs]
        label = f"BB{node}\\n" + "\\n".join(label_lines)
        lines.append(f'  node{node} [label="{label}"];')
    for src, dst in cfg.edges:
        lines.append(f'  node{src} -> node{dst};')
    lines.append("}")
    return "\n".join(lines)

def visualize_graph(cfg, filename="cfg.png"):
    """Visualize the CFG using the graphviz package (no pygraphviz needed)."""
    try:
        dot_str = cfg_to_dot(cfg)
        base_filename = os.path.splitext(filename)[0]
        src = Source(dot_str, filename=base_filename, format="png")
        output_path = src.render(cleanup=True)
        if output_path != filename:
            os.replace(output_path, filename)
        print(f"CFG visualization saved as '{filename}'")
        return True
    except Exception as e:
        print(f"Error visualizing CFG with graphviz package: {e}")
        import traceback
        traceback.print_exc()
        return False

def textualize_graph(cfg):
    text = "Control Flow Graph\n"
    for node in sorted(cfg.nodes):
        text += f'BB{node} '
        successors = list(cfg.successors(node))
        if successors:
            text += ", ".join([f'->BB{x}' for x in successors])
        text += "\n"
        instr_texts = [instr.getText() if hasattr(instr, 'getText') else str(instr) 
                       for instr in cfg.nodes[node].get("instrs", [])]
        text += "\n".join(instr_texts)
        text += "\n\n"
    return text

# ---------------------------------------------------------------------------
# CFG construction from IR instructions.
# ---------------------------------------------------------------------------
def build_cfg(instrs):
    if not instrs:
        raise Exception("No instructions to process")
    
    label_to_index = {}
    for i, instr in enumerate(instrs):
        text = instr.getText().strip()
        if text.endswith(":"):
            label_name = text[:-1].strip()
            label_to_index[label_name] = i
    
    leaders = set()
    leaders.add(0)
    for i, instr in enumerate(instrs):
        text = instr.getText()
        if "goto" in text:
            tokens = text.split()
            target = tokens[-1]
            if target in label_to_index:
                leaders.add(label_to_index[target])
            if i + 1 < len(instrs):
                leaders.add(i + 1)
    leaders.add(len(instrs))
    sorted_leaders = sorted(leaders)
    
    basic_blocks = {}
    for idx in range(len(sorted_leaders) - 1):
        start = sorted_leaders[idx]
        end = sorted_leaders[idx + 1]
        basic_blocks[start] = instrs[start:end]
    
    cfg = nx.DiGraph()
    for leader, block in basic_blocks.items():
        cfg.add_node(leader, instrs=block)
    
    sorted_nodes = sorted(basic_blocks.keys())
    for i, leader in enumerate(sorted_nodes):
        block = basic_blocks[leader]
        if not block:
            continue
        last_instr = block[-1].getText()
        if "goto" in last_instr:
            tokens = last_instr.split()
            target = tokens[-1]
            if target in label_to_index:
                cfg.add_edge(leader, label_to_index[target])
            if "if" in last_instr:
                if i + 1 < len(sorted_nodes):
                    cfg.add_edge(leader, sorted_nodes[i + 1])
        else:
            if i + 1 < len(sorted_nodes):
                cfg.add_edge(leader, sorted_nodes[i + 1])
    
    return cfg

# ---------------------------------------------------------------------------
# Dataflow Analysis - Constant Propagation
# ---------------------------------------------------------------------------
def dataflow_analysis(cfg):
    """
    Perform constant propagation optimization on the CFG.
    Identifies variables assigned constant values and propagates them.
    Also evaluates constant expressions at compile time.
    """
    # Map of variable -> constant value (None if not constant or unknown)
    constants = {}
    
    # Analyze and propagate constants
    changed = True
    while changed:
        changed = False
        
        # For each block in the CFG
        for node in sorted(cfg.nodes):
            block = cfg.nodes[node].get("instrs", [])
            new_instrs = []
            
            # Process each instruction
            for instr in block:
                text = instr.getText()
                
                # Fix spacing issues in control flow instructions
                if "if" in text and "goto" in text and " " not in text.split("if")[1].split("goto")[0]:
                    # Add space before comparison operator
                    for op in [">", "<", "=", ">=", "<="]:
                        text = text.replace(op, f" {op} ")
                    # Fix any double spaces
                    while "  " in text:
                        text = text.replace("  ", " ")
                    # Add space before goto
                    if "goto" in text and " goto " not in text:
                        text = text.replace("goto", " goto ")
                
                # Fix spacing in regular goto
                if "goto" in text and "if" not in text and " goto " not in text:
                    text = text.replace("goto", " goto ")
                
                # Handle variable assignments with constant expressions
                if ":=" in text and "goto" not in text:
                    parts = text.split(":=", 1)
                    lhs = parts[0].strip()
                    rhs = parts[1].strip()
                    
                    # Case 1: Direct constant assignment
                    if rhs.isdigit():
                        constants[lhs] = int(rhs)
                    
                    # Case 2: Assignment from another constant variable
                    elif rhs in constants and constants[rhs] is not None:
                        new_text = f"{lhs} := {constants[rhs]}"
                        if new_text != text:
                            changed = True
                            text = new_text
                            constants[lhs] = constants[rhs]
                    
                    # Case 3: Arithmetic expression that might be evaluable
                    elif any(op in rhs for op in ["+", "-", "*", "/"]):
                        # First substitute known constants into the expression
                        expr = rhs
                        for var, val in constants.items():
                            if val is not None:
                                pattern = r'\b' + re.escape(var) + r'\b'
                                expr = re.sub(pattern, str(val), expr)
                        
                        # Try to evaluate the expression if it's now all constants
                        try:
                            # Extract operands and operator
                            # Look for patterns like "5 + 3", "10 - 2", etc.
                            match = re.match(r'(\d+)\s*([+\-*/])\s*(\d+)$', expr)
                            if match:
                                a, op, b = match.groups()
                                a, b = int(a), int(b)
                                
                                # Evaluate the expression
                                if op == '+':
                                    result = a + b
                                elif op == '-':
                                    result = a - b
                                elif op == '*':
                                    result = a * b
                                elif op == '/' and b != 0:
                                    result = a // b  # Integer division for IR
                                else:
                                    raise ValueError("Invalid operation")
                                
                                # Update the instruction and mark variable as constant
                                new_text = f"{lhs} := {result}"
                                if new_text != text:
                                    changed = True
                                    text = new_text
                                    constants[lhs] = result
                        except:
                            # If evaluation fails, variable is no longer constant
                            constants[lhs] = None
                    else:
                        # Not a constant assignment
                        constants[lhs] = None
                
                # For non-assignment expressions (e.g., in conditions), just substitute constants
                elif any(op in text for op in ["+", "-", "*", "/", "<", ">", "="]):
                    new_text = text
                    for var, val in constants.items():
                        if val is not None:
                            pattern = r'\b' + re.escape(var) + r'\b'
                            new_text = re.sub(pattern, str(val), new_text)
                    
                    if new_text != text:
                        changed = True
                        text = new_text
                
                # Create a new instruction with the possibly modified text
                new_instr = SimpleInstruction(text)
                new_instrs.append(new_instr)
            
            # Update the block with new instructions
            cfg.nodes[node]["instrs"] = new_instrs
    
    return cfg

# Helper class to create instruction objects with getText() method
class SimpleInstruction:
    def __init__(self, text):
        self.text = text
    
    def getText(self):
        return self.text

# ---------------------------------------------------------------------------
# Reconstruct the optimized IR from the CFG
# ---------------------------------------------------------------------------
def reconstruct_ir(cfg):
    lines = []
    for node in sorted(cfg.nodes):
        block_instrs = cfg.nodes[node].get('instrs', [])
        lines.extend([instr.getText() for instr in block_instrs])
    return "\n".join(lines)

# ---------------------------------------------------------------------------
# Main Driver
# ---------------------------------------------------------------------------
def main():
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = StdinStream()
    
    lexer = SimpleIRLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SimpleIRParser(stream)
    tree = parser.unit()
    
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Syntax errors encountered in the input.")
        exit(1)
    
    walker = ParseTreeWalker()
    irl = IRList()
    walker.walk(irl, tree)
    instrs = irl.instr
    logging.debug(f"Collected {len(instrs)} instructions.")
    
    cfg = build_cfg(instrs)
    logging.debug("CFG built successfully.")
    print(textualize_graph(cfg))
    
    cfg = dataflow_analysis(cfg)
    logging.debug("Dataflow analysis (constant propagation) completed.")
    
    reconstructed_ir_code = reconstruct_ir(cfg)
    print("Reconstructed IR (from CFG):")
    print(reconstructed_ir_code)
    
    visualize_graph(cfg)

if __name__ == "__main__":
    main()
