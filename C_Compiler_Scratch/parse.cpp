#include "parse.h"
#include <iostream>
#include <string>

Parser::Parser(Lexer& lex, Emitter& emit) 
    : lexer(lex), 
      emitter(emit), 
      currentToken("", TokenType::EOF_TOKEN), 
      peekToken("", TokenType::EOF_TOKEN) {
    nextToken();
    nextToken(); // Call twice to initialize currentToken and peekToken
}

void Parser::nextToken() {
    currentToken = peekToken;
    peekToken = lexer.getToken();
}

void Parser::match(TokenType kind) {
    if (currentToken.getKind() != kind) {
        abort("Expected " + std::to_string(static_cast<int>(kind)) + 
              ", got " + std::to_string(static_cast<int>(currentToken.getKind())));
    }
    nextToken();
}

void Parser::abort(const std::string& message) {
    std::cerr << "Error! " << message << std::endl;
    exit(1);
}

void Parser::program() {
    // Write the C program header
    emitter.emitLine("#include <stdio.h>");
    emitter.emitLine("int main(void) {");
    
    // Skip leading newlines if any
    while (currentToken.getKind() == TokenType::NEWLINE) {
        nextToken();
    }
    
    // Parse statements until the end of the file
    while (currentToken.getKind() != TokenType::EOF_TOKEN) {
        statement();
        
        // Skip any newlines between statements
        while (currentToken.getKind() == TokenType::NEWLINE) {
            nextToken();
        }
    }
    
    // Write the C program footer
    emitter.emitLine("    return 0;");
    emitter.emitLine("}");
}

void Parser::statement() {
    // Check the first token to determine statement type
    
    // "PRINT" (expression | string)
    if (currentToken.getKind() == TokenType::PRINT) {
        nextToken();
        
        if (currentToken.getKind() == TokenType::STRING) {
            // Simple string
            emitter.emitLine("    printf(\"" + currentToken.getText() + "\\n\");");
            nextToken();
        } else {
            // Expression
            emitter.emit("    printf(\"%d\\n\", ");
            expression();
            emitter.emitLine(");");
        }
    }
    // "IF" comparison "THEN" nl {statement} "ENDIF"
    else if (currentToken.getKind() == TokenType::IF) {
        nextToken();
        emitter.emit("    if(");
        comparison();
        
        match(TokenType::THEN);
        emitter.emitLine(") {");
        
        // Skip any newlines after THEN
        while (currentToken.getKind() == TokenType::NEWLINE) {
            nextToken();
        }
        
        // Zero or more statements in the body
        while (currentToken.getKind() != TokenType::ENDIF) {
            statement();
            
            // Skip any newlines between statements
            while (currentToken.getKind() == TokenType::NEWLINE) {
                nextToken();
            }
        }
        
        match(TokenType::ENDIF);
        emitter.emitLine("    }");
    }
    // "WHILE" comparison "REPEAT" nl {statement} "ENDWHILE"
    else if (currentToken.getKind() == TokenType::WHILE) {
        nextToken();
        emitter.emit("    while(");
        comparison();
        
        match(TokenType::REPEAT);
        emitter.emitLine(") {");
        
        // Skip any newlines after REPEAT
        while (currentToken.getKind() == TokenType::NEWLINE) {
            nextToken();
        }
        
        // Zero or more statements in the body
        while (currentToken.getKind() != TokenType::ENDWHILE) {
            statement();
            
            // Skip any newlines between statements
            while (currentToken.getKind() == TokenType::NEWLINE) {
                nextToken();
            }
        }
        
        match(TokenType::ENDWHILE);
        emitter.emitLine("    }");
    }
    // "LET" ident = expression
    else if (currentToken.getKind() == TokenType::LET) {
        nextToken();
        
        if (currentToken.getKind() != TokenType::IDENT) {
            abort("Expected identifier after 'LET'");
        }
        
        std::string varName = currentToken.getText();
        nextToken();
        
        match(TokenType::EQ);
        
        emitter.emit("    " + varName + " = ");
        expression();
        emitter.emitLine(";");
    }
    // "INPUT" ident
    else if (currentToken.getKind() == TokenType::INPUT) {
        nextToken();
        
        if (currentToken.getKind() != TokenType::IDENT) {
            abort("Expected identifier after 'INPUT'");
        }
        
        std::string varName = currentToken.getText();
        emitter.emitLine("    printf(\"Input: \");");
        emitter.emitLine("    scanf(\"%d\", &" + varName + ");");
        nextToken();
    }
    // This is not a valid statement
    else {
        abort("Invalid statement at: " + currentToken.getText());
    }
    
    // Newline - make this optional by checking if the current token is a newline
    if (currentToken.getKind() == TokenType::NEWLINE) {
        nextToken();
    }
    // If not a newline, we don't need to match it
}

void Parser::comparison() {
    expression();
    
    // Must be a comparison operator
    if (currentToken.getKind() == TokenType::EQEQ || currentToken.getKind() == TokenType::NOTEQ ||
        currentToken.getKind() == TokenType::LT || currentToken.getKind() == TokenType::LTEQ ||
        currentToken.getKind() == TokenType::GT || currentToken.getKind() == TokenType::GTEQ) {
        
        std::string op;
        switch (currentToken.getKind()) {
            case TokenType::EQEQ:  op = "=="; break;
            case TokenType::NOTEQ: op = "!="; break;
            case TokenType::LT:    op = "<"; break;
            case TokenType::LTEQ:  op = "<="; break;
            case TokenType::GT:    op = ">"; break;
            case TokenType::GTEQ:  op = ">="; break;
            default: break; // Never reached
        }
        
        nextToken();
        emitter.emit(op + " ");
        expression();
    } else {
        abort("Expected comparison operator");
    }
}

void Parser::expression() {
    term();
    
    // Can have 0 or more +/- operations
    while (currentToken.getKind() == TokenType::PLUS || currentToken.getKind() == TokenType::MINUS) {
        emitter.emit(currentToken.getText() + " ");
        nextToken();
        term();
    }
}

void Parser::term() {
    unary();
    
    // Can have 0 or more *// operations
    while (currentToken.getKind() == TokenType::ASTERISK || currentToken.getKind() == TokenType::SLASH) {
        emitter.emit(currentToken.getText() + " ");
        nextToken();
        unary();
    }
}

void Parser::unary() {
    // Optional unary +/-
    if (currentToken.getKind() == TokenType::PLUS || currentToken.getKind() == TokenType::MINUS) {
        emitter.emit(currentToken.getText());
        nextToken();
    }
    
    primary();
}

void Parser::primary() {
    if (currentToken.getKind() == TokenType::NUMBER) {
        emitter.emit(currentToken.getText());
        nextToken();
    } else if (currentToken.getKind() == TokenType::IDENT) {
        emitter.emit(currentToken.getText());
        nextToken();
    } else {
        abort("Unexpected token: " + currentToken.getText());
    }
}
