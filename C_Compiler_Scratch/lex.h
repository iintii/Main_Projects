#pragma once
#include "token.h"
#include <string>
#include <iostream>

class Lexer {
private:
    std::string source;
    char curChar;
    int curPos;

    void nextChar();
    char peek() const;
    void skipWhitespace();
    void skipComment();
    void abort(const std::string& message) const;

public:
    Lexer(const std::string& source);
    Token getToken();
};
