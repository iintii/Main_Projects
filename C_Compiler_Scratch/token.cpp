#include "token.h"
#include <map>

Token::Token(const std::string& tokenText, TokenType tokenKind) 
    : text(tokenText), kind(tokenKind) {}

std::string Token::getText() const {
    return text;
}

TokenType Token::getKind() const {
    return kind;
}

TokenType Token::checkIfKeyword(const std::string& tokenText) {
    static const std::map<std::string, TokenType> keywords = {
        {"LABEL", TokenType::LABEL},
        {"GOTO", TokenType::GOTO},
        {"PRINT", TokenType::PRINT},
        {"INPUT", TokenType::INPUT},
        {"LET", TokenType::LET},
        {"IF", TokenType::IF},
        {"THEN", TokenType::THEN},
        {"ENDIF", TokenType::ENDIF},
        {"WHILE", TokenType::WHILE},
        {"REPEAT", TokenType::REPEAT},
        {"ENDWHILE", TokenType::ENDWHILE}
    };

    auto it = keywords.find(tokenText);
    if (it != keywords.end()) {
        return it->second;
    }

    return static_cast<TokenType>(0); // Null equivalent
}
