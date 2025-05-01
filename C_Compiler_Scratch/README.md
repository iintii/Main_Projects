🛠️ Teeny Tiny Compiler
=======================

A minimalist compiler that translates a custom scripting language into C code, built entirely from scratch in C++!

🚀 Overview
-----------

Teeny Tiny Compiler is a straightforward yet powerful project demonstrating the fundamentals of compiler construction. It takes a custom language (with commands like LET, WHILE, IF, PRINT, etc.) and generates equivalent C code that can be compiled and run with any standard C compiler.

### Key Components:

-   **Lexical Analysis ([lex.cpp](vscode-file://vscode-app/c:/Users/brody/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html))**: Breaks source code into tokens
-   **Token Handling ([token.cpp](vscode-file://vscode-app/c:/Users/brody/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html))**: Defines and manages token types
-   **Parsing (`parse.cpp`)**: Implements grammar rules via recursive descent
-   **Code Emission ([emit.cpp](vscode-file://vscode-app/c:/Users/brody/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html))**: Generates the target C code
-   **Main Driver ([main.cpp](vscode-file://vscode-app/c:/Users/brody/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html))**: Orchestrates the compilation process

⚙️ How It Works
---------------

1.  The **Lexer** reads and tokenizes the source file into recognizable symbols
2.  The **Parser** validates grammar and builds a structural representation
3.  The **Emitter** transforms this structure into valid C code
4.  The output is saved as [out.c](vscode-file://vscode-app/c:/Users/brody/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) which can be compiled with a standard C compiler

🏗️ Project Structure
---------------------
```
├── main.cpp      # Main driver that orchestrates the compilation process

├── lex.cpp       # Lexical analyzer that converts source to tokens

├── token.cpp     # Token definitions and keyword checking

├── parse.cpp     # Parser that implements grammar rules

├── emit.cpp      # Emitter that generates the output C code

├── Makefile      # Build configuration

└── input.txt     # Example source code in the custom language
```

🔧 Building and Running
-----------------------
```
# Build the compiler

make

# Run the compiler on an input file

./compiler input.txt

# Compile the generated C code

gcc -o program out.c

# Run the resulting program

./program
```

📝 Input Code Example
---------------
```
LET a = 0

WHILE a < 1 REPEAT

    PRINT "Enter number of scores: "

    INPUT a

ENDWHILE

LET b = 0

LET s = 0

PRINT "Enter one value at a time: "

WHILE b < a REPEAT

    INPUT c

    LET s = s + c

    LET b = b + 1

ENDWHILE

PRINT "Average: "

PRINT s / a
```
