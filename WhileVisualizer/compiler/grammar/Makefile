GRAMMAR = While
ANTLR = antlr-4.9.1-complete.jar

all: $(GRAMMAR)Parser.py

$(GRAMMAR)Parser.py: $(GRAMMAR).g4 $(ANTLR)
	java -cp "$(ANTLR);." org.antlr.v4.Tool -Dlanguage=Python3 -visitor $<

$(ANTLR):
	powershell -Command "Invoke-WebRequest -Uri https://www.antlr.org/download/$(ANTLR) -OutFile $(ANTLR)"

clean:
	cmd /C del /Q $(GRAMMAR).interp $(GRAMMAR)Lexer.interp $(GRAMMAR)Lexer.py $(GRAMMAR)Lexer.tokens $(GRAMMAR)Listener.py $(GRAMMAR)Parser.py $(GRAMMAR)Visitor.py $(GRAMMAR).tokens

clobber: clean
	cmd /C del /Q $(ANTLR)
