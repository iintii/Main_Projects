#pragma once
#include <string>

// TokenType is our enum for all the types of tokens
enum class TokenType {
    EOF_TOKEN = -1,
    NEWLINE = 0,
    NUMBER = 1,
    IDENT = 2,
    STRING = 3,
    // Keywords
    LABEL = 101,
    GOTO = 102,
    PRINT = 103,
    INPUT = 104,
    LET = 105,
    IF = 106,
    THEN = 107,
    ENDIF = 108,
    WHILE = 109,
    REPEAT = 110,
    ENDWHILE = 111,
    // Operators
    EQ = 201,
    PLUS = 202,
    MINUS = 203,
    ASTERISK = 204,
    SLASH = 205,
    EQEQ = 206,
    NOTEQ = 207,
    LT = 208,
    LTEQ = 209,
    GT = 210,
    GTEQ = 211
};

// Token contains the original text and the type of token
class Token {
private:
    std::string text;
    TokenType kind;

public:
    Token(const std::string& tokenText, TokenType tokenKind);
    std::string getText() const;
    TokenType getKind() const;
    static TokenType checkIfKeyword(const std::string& tokenText);
};
