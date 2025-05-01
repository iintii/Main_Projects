CXX = g++
CXXFLAGS = -std=c++11 -Wall -Wextra -pedantic
SOURCES = main.cpp lex.cpp token.cpp emit.cpp parse.cpp
OBJECTS = $(SOURCES:.cpp=.o)
EXECUTABLE = compiler

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS)
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $@

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(OBJECTS) $(EXECUTABLE)

.PHONY: all clean
