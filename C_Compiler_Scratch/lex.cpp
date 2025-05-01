#include "lex.h"
#include <iostream>
#include <map>
#include <cctype>

Lexer::Lexer(const std::string& src) : source(src + '\n'), curChar('\0'), curPos(-1) {
    nextChar();
}

void Lexer::nextChar() {
    curPos++;
    if (curPos >= static_cast<int>(source.length())) {
        curChar = '\0'; // EOF
    } else {
        curChar = source[curPos];
    }
}

char Lexer::peek() const {
    if (curPos + 1 >= static_cast<int>(source.length())) {
        return '\0';
    }
    return source[curPos + 1];
}

void Lexer::abort(const std::string& message) const {
    std::cerr << "Lexing error. " << message << std::endl;
    exit(1);
}

void Lexer::skipWhitespace() {
    while (curChar == ' ' || curChar == '\t' || curChar == '\r') {
        nextChar();
    }
}

void Lexer::skipComment() {
    if (curChar == '#') {
        while (curChar != '\n') {
            nextChar();
        }
    }
}

Token Lexer::getToken() {
    skipWhitespace();
    skipComment();

    // Maps for token types
    static const std::map<char, TokenType> singleCharTokens = {
        {'+', TokenType::PLUS},
        {'-', TokenType::MINUS},
        {'*', TokenType::ASTERISK},
        {'/', TokenType::SLASH},
        {'=', TokenType::EQ},
        {'<', TokenType::LT},
        {'>', TokenType::GT}
    };

    static const std::map<std::string, TokenType> multiCharTokens = {
        {"==", TokenType::EQEQ},
        {">=", TokenType::GTEQ},
        {"<=", TokenType::LTEQ},
        {"!=", TokenType::NOTEQ}
    };

    // Check for operators
    if (singleCharTokens.find(curChar) != singleCharTokens.end()) {
        std::string combinedChars = std::string(1, curChar) + peek();
        
        if (curChar == '!' && peek() != '=') {
            abort("Expected !=, got !" + std::string(1, peek()));
        }

        if (multiCharTokens.find(combinedChars) != multiCharTokens.end()) {
            Token token(combinedChars, multiCharTokens.at(combinedChars));
            nextChar(); // Move to the second character
            nextChar(); // Move past the second character
            return token;
        }

        // Single character token
        Token token(std::string(1, curChar), singleCharTokens.at(curChar));
        nextChar();
        return token;
    }
    
    // Check for string
    if (curChar == '\"') {
        nextChar();
        int startPos = curPos;
        
        while (curChar != '\"') {
            // Don't allow special characters in the string
            if (curChar == '\r' || curChar == '\n' || curChar == '\t' || curChar == '%') {
                abort("Illegal character in string.");
            }
            nextChar();
        }
        
        std::string tokenText = source.substr(startPos, curPos - startPos);
        Token token(tokenText, TokenType::STRING);
        nextChar();
        return token;
    }
    
    // Check for number
    if (isdigit(curChar)) {
        int startPos = curPos;
        
        while (isdigit(peek())) {
            nextChar();
        }
        
        if (peek() == '.') {
            nextChar();
            
            // Must have at least one digit after decimal
            if (!isdigit(peek())) {
                abort("Illegal character in number.");
            }
            
            while (isdigit(peek())) {
                nextChar();
            }
        }
        
        std::string tokenText = source.substr(startPos, curPos - startPos + 1);
        Token token(tokenText, TokenType::NUMBER);
        nextChar();
        return token;
    }
    
    // Check for identifier or keyword
    if (isalpha(curChar)) {
        int startPos = curPos;
        
        while (isalnum(peek())) {
            nextChar();
        }
        
        std::string tokenText = source.substr(startPos, curPos - startPos + 1);
        TokenType keyword = Token::checkIfKeyword(tokenText);
        
        if (static_cast<int>(keyword) == 0) { // Not a keyword
            Token token(tokenText, TokenType::IDENT);
            nextChar();
            return token;
        } else {
            Token token(tokenText, keyword);
            nextChar();
            return token;
        }
    }
    
    // Check for newline
    if (curChar == '\n') {
        Token token("\n", TokenType::NEWLINE);
        nextChar();
        return token;
    }
    
    // Check for EOF
    if (curChar == '\0') {
        Token token("", TokenType::EOF_TOKEN);
        return token;
    }
    
    // Unknown token
    abort("Unknown token: " + std::string(1, curChar));
    
    // This will never be reached but keeps the compiler happy
    return Token("", TokenType::EOF_TOKEN);
}
