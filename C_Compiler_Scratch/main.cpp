#include "lex.h"
#include "emit.h"
#include "parse.h"
#include <iostream>
#include <fstream>
#include <sstream>

int main(int argc, char* argv[]) {
    std::cout << "Teeny Tiny Compiler" << std::endl;
    
    if (argc != 2) {
        std::cerr << "Error: Compiler needs source file as argument." << std::endl;
        return 1;
    }
    
    std::ifstream inputFile(argv[1]);
    if (!inputFile) {
        std::cerr << "Error: Cannot open source file." << std::endl;
        return 1;
    }
    
    std::stringstream buffer;
    buffer << inputFile.rdbuf();
    std::string source = buffer.str();
    
    // Print the source for debugging
    std::cout << "\nSource code:\n" << source << std::endl;
    
    // Initialize the lexer, emitter, and parser
    Lexer lexer(source);
    Emitter emitter("out.c");
    
    // Debug: Print all tokens before parsing
    std::cout << "\nTokens:\n";
    Lexer debugLexer(source);
    Token token = debugLexer.getToken();
    while (token.getKind() != TokenType::EOF_TOKEN) {
        std::cout << "Token: " << token.getText() 
                  << " (Type: " << static_cast<int>(token.getKind()) << ")\n";
        token = debugLexer.getToken();
    }
    std::cout << std::endl;
    
    Parser parser(lexer, emitter);
    
    parser.program(); // Start the parser
    
    // Instead of writing to file, display in terminal
    std::cout << "\nOutput code: ---\n" << emitter.getCode() << std::endl;
    
    std::cout << "Compiling completed." << std::endl;
    return 0;
}
