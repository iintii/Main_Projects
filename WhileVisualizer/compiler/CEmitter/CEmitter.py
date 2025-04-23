import re
from io import StringIO

class CEmitter:
    def __init__(self):
        self.variable_types = {}  # Maps variable names to C types
        self.declared_vars = set()  # Track declared variables
        
    def emit(self, ir_code, output_stream):
        """Convert IR code to C code"""
        lines = ir_code.strip().split('\n')
        
        # Extract function definition if present
        function_name = "main"
        for i, line in enumerate(lines):
            if line.startswith("function "):
                function_name = line.split()[1]
                lines = lines[i+1:]
                break
        
        # First pass: analyze variables to determine types
        self._analyze_variables(lines)
        
        # Write C file header
        output_stream.write("#include <stdio.h>\n")
        output_stream.write("#include <stdbool.h>\n\n")
        
        # Start main function
        output_stream.write(f"int {function_name}() {{\n")
        
        # Declare variables
        self._write_variable_declarations(output_stream)
        
        # Process each line of IR code
        for line in lines:
            if line.startswith("#") or not line.strip():
                continue  # Skip comments and empty lines
                
            if line.startswith("end function"):
                continue  # Skip end function marker
            elif line.startswith("return"):
                c_line = self._translate_return(line)
            elif ":" in line and not ":=" in line:
                c_line = self._translate_label(line)
            elif line.startswith("if ") and " goto " in line:
                c_line = self._translate_conditional_goto(line)
            elif line.startswith("goto "):
                c_line = self._translate_goto(line)
            elif ":=" in line:
                c_line = self._translate_assignment(line)
            else:
                # Instead of adding a comment, just skip this line
                continue
            
            # Skip any generated comment lines
            if c_line.strip().startswith("//"):
                continue
                
            output_stream.write(c_line + "\n")
        
        # Close function
        output_stream.write("}\n")
    
    def _analyze_variables(self, ir_lines):
        """Analyze IR code to determine variable types"""
        for line in ir_lines:
            # Skip function boundaries, labels, gotos
            if line.startswith(("function", "end function", "return", "goto")) or ((":" in line and not ":=" in line)):
                continue
                
            # Analyze assignments
            if ":=" in line:
                lhs, rhs = line.split(":=", 1)
                var_name = lhs.strip()
                
                # Determine type from RHS
                if re.search(r'[0-9]+', rhs):
                    self.variable_types[var_name] = "int"
                elif "true" in rhs or "false" in rhs or " = 0" in rhs or " = 1" in rhs:
                    self.variable_types[var_name] = "bool"
                else:
                    # Default to int if we can't determine
                    self.variable_types[var_name] = "int"
    
    def _write_variable_declarations(self, output_stream):
        """Write variable declarations at the beginning of the function"""
        for var, var_type in self.variable_types.items():
            output_stream.write(f"    {var_type} {var};\n")
        output_stream.write("\n")
    
    def _translate_assignment(self, line):
        """Translate IR assignment to C assignment"""
        lhs, rhs = line.split(":=", 1)
        var_name = lhs.strip()
        rhs = rhs.strip()
        
        # Replace IR true/false with C true/false
        rhs = rhs.replace(" = 0", " == 0").replace(" = 1", " == 1")
        
        return f"    {var_name} = {rhs};"
    
    def _translate_label(self, line):
        """Translate IR label to C label"""
        label_name = line.strip().rstrip(':')
        return f"{label_name}:"
    
    def _translate_goto(self, line):
        """Translate IR goto to C goto"""
        goto_pattern = re.compile(r'goto\s*(\w+)')
        match = goto_pattern.search(line)
        if match:
            label = match.group(1)
            return f"    goto {label};"
        else:
            return ""  # Return empty string instead of a comment

    def _translate_conditional_goto(self, line):
        """Translate IR conditional goto to C if statement with goto"""
        if_goto_pattern = re.compile(r'if\s*(.+?)\s*goto\s*(\w+)')
        match = if_goto_pattern.search(line)
        
        if not match:
            return ""  # Return empty string instead of a comment
        
        condition = match.group(1).strip()
        label = match.group(2).strip()
        
        # Add spaces around operators for readability
        condition = re.sub(r'([<>=])', r' \1 ', condition)
        condition = re.sub(r'\s+', ' ', condition)
        condition = re.sub(r'(\w+)\+(\w+)', r'\1 + \2', condition)
        condition = re.sub(r'(\w+)-(\w+)', r'\1 - \2', condition)
        
        # Replace = with == for comparison
        condition = re.sub(r'([^=])=([^=])', r'\1==\2', condition)
        
        return f"    if ({condition}) goto {label};"
    
    def _translate_return(self, line):
        """Translate IR return to C return"""
        parts = line.split()
        if len(parts) > 1:
            return f"    return {parts[1]};"
        else:
            return f"    return 0;"

def emit_c_code(ir_code, output_stream):
    """Convert IR code to C code and write to output stream"""
    emitter = CEmitter()
    emitter.emit(ir_code, output_stream)

# Command-line interface if run directly
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            ir_code = f.read()
    else:
        ir_code = sys.stdin.read()
    
    emit_c_code(ir_code, sys.stdout)