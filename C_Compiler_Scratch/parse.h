#pragma once
#include "lex.h"
#include "emit.h"

class Parser {
private:
    Lexer& lexer;
    Emitter& emitter;
    
    Token currentToken;
    Token peekToken;
    
    void nextToken();
    void match(TokenType kind);
    void abort(const std::string& message);
    
    // Grammar productions
    void statement();
    void expression();
    void term();
    void unary();
    void primary();
    void comparison();
    
    // Other grammar-related methods would be declared here

public:
    Parser(Lexer& lexer, Emitter& emitter);
    void program();
};
