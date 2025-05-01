from antlr4.tree.Trees import Trees
import sys #We are interacting with the system like reading in input files
from antlr4 import * #we can access inputstream / file stream which will help antlr read the inputfiles. Inputstream reads from texts while filestream read input from a file path. 
from WhileLexer import WhileLexer
from WhileParser import WhileParser

def main():
    #input reading
    if len(sys.argv) > 1: #if you run python script.py arg1 arg2, sys.argv will be ['script.py', 'arg1', 'arg2']. so its a list
        input_stream = FileStream(sys.argv[1]) #essentially choosing the input.txt from the list
    else: #if no input file is found, then read from standard input from user
        input_stream = InputStream(sys.stdin.read()) #stdin is standard input from user to be read

    lexer = WhileLexer(input_stream) #insert input file into lexer
    tokens = CommonTokenStream(lexer)  #lexer and token are paired. token is an instance of CommonTokenStream. Its a more advanced daata sctructure than a list but does hold all the tokens created
    parser = WhileParser(tokens)
    tree = parser.program() #If your grammar’s root rule is not program, replace parser.program() with your rule (e.g., parser.start()).

    #parse tree created
    #print(tree.toStringTree(recog=parser)) #converts parse tree into readable string. recog=parser: Tells ANTLR to use the parser’s rule names (like program, statement) in the output.
    print(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__': #In summary, this block ensures that your main() function is only called when the script is run directly, and not when it's imported elsewhere. It's a good practice
    main()

