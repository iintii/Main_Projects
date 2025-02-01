import sys
import enum

class Lexer:

    '''The Lexer will be responsible for Tokenizing the source input language. This is a structurally sound, yet fairly simple implimentation where the input code is processed character by character and classified into tokens. For this implimentation, Final State Machines and Regex libraries will not be utilized.
    '''

    def __init__(self, source):
        self.source = source + '\n' # New line added to the end of input to make "End of Line" parsing easier. 
        self.curChar = ''  #Initialize current character and current position
        self.curPos = -1   
        self.nextChar() #Everytime the lexer is initialized we start at the first character.

    def nextChar(self):
        '''Simple function to update the curChar variable with the next character in the source code.
        '''
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0'  # EOF
        else:
            self.curChar = self.source[self.curPos]

    
    def peek(self):
        '''Used to check what the next character in the source code is without assigning / processing it ie without "consuming" the character.
        '''
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos+1]

    #Error function for when we want to return error messages for undesirable codes.
    def abort(self, message):
        sys.exit("Lexing error. " + message)

    def getToken(self):
        '''
        Primary function in the lexer. Will iterate through the whole input code one character at a time and classify it. Will handle various token types, such as keywords, identifiers, operators etc. The ultimate goal of the function is to store each of the character symbols and their respective types in a Token object and return that object to the parser for further processing. Only 1 Token object is returned at a time by the lexer.
        '''
        self.skipWhitespace()
        self.skipComment()
        token = None

        #OPERATOR PROCESSING
        #Because we are performing similar tasks for each operator, it is easier to use a Hashmap
        single_char_tokens = {'+': TokenType.PLUS, 
                              '-': TokenType.MINUS, 
                              '*': TokenType.ASTERISK, 
                              '/': TokenType.SLASH, 
                              '=': TokenType.EQ, 
                              '<': TokenType.LT, 
                              '>': TokenType.GT}

        mult_char_tokens = {'==': TokenType.EQEQ, 
                            '>=': TokenType.GTEQ, 
                            '<=': TokenType.LTEQ}

        if self.curChar in single_char_tokens:
            combined_chars = self.curChar + self.peek()

            #---------------------------------------------------------
            if self.curChar == '!' and self.peek() != '=':
                self.abort("Expected !=, got !" + self.peek())
            else:
                token = Token(self.curChar + self.peek(), TokenType.NOTEQ)
            #----------------------------------------------------------

            if combined_chars in mult_char_tokens:
                token = Token(combined_chars, mult_char_tokens[combined_chars])

                self.nextChar() #Moving to the second character. Note: nextChar() is called at the end of the function again to moved to unprocessed characters. 

            token = Token(self.curChar, single_char_tokens[self.curChar]) 
        
        #STRING PROCESSING
        elif self.curChar == '\"':
            # String extraction from source code using indexing
            self.nextChar()
            startPos = self.curPos

            while self.curChar != '\"':
                # Don't allow special characters in the string. 
                if self.curChar in ['\r', '\n', '\t', '%']:
                    self.abort("Illegal character in string.")
                self.nextChar()

            tokText = self.source[startPos : self.curPos] 
            token = Token(tokText, TokenType.STRING)

        #DIGIT PROCESSING
        elif self.curChar.isdigit():
            #Number extraction using indexing
            startPos = self.curPos
            while self.peek().isdigit():
                self.nextChar()
            if self.peek() == '.': 
                self.nextChar()

                # Must have at least one digit after decimal.
                if not self.peek().isdigit(): 
                    self.abort("Illegal character in number.")
                while self.peek().isdigit():
                    self.nextChar()

            tokText = self.source[startPos : self.curPos + 1] # Get the substring.
            token = Token(tokText, TokenType.NUMBER)

        #ALNUM and KEYWORD PROCESSING
        elif self.curChar.isalpha():
            # Get all consecutive alpha numeric characters.
            startPos = self.curPos
            while self.peek().isalnum():
                self.nextChar()
            # Check if the token is in the list of keywords.
            tokText = self.source[startPos : self.curPos + 1] 
            keyword = Token.checkIfKeyword(tokText)
            if keyword == None: 
                token = Token(tokText, TokenType.IDENT)
            else:  
                token = Token(tokText, keyword)

        #NEWLINE PROCESSING
        elif self.curChar == '\n':
            
            token = Token('\n', TokenType.NEWLINE)

        #END OF LINE PROCESSING
        elif self.curChar == '\0':
             # EOF.
            token = Token('', TokenType.EOF)

        else:
            self.abort("Unknown token: " + self.curChar)

        self.nextChar()
        return token

    # Skip whitespace except newlines
    def skipWhitespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextChar()

    #Skip comments
    def skipComment(self): 
        if self.curChar == '#':
            while self.curChar != '\n':
                self.nextChar()

# Token contains the original text and the type of token
class Token:   
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText   # The token's actual text from the source code
        self.kind = tokenKind   # The TokenType that this token is classified as
    
    def checkIfKeyword(tokenText):
        for kind in TokenType:
            # Relies on all keyword enum values being between 100 and 200.
            if kind.name == tokenText and 100 <= kind.value < 200:
                return kind
        return None


# TokenType is our enum for all the types of tokens.
class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3
    # Keywords.
    LABEL = 101
    GOTO = 102
    PRINT = 103
    INPUT = 104
    LET = 105
    IF = 106
    THEN = 107
    ENDIF = 108
    WHILE = 109
    REPEAT = 110
    ENDWHILE = 111
    # Operators.
    EQ = 201  
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211