#pragma once
#include <string>
#include <fstream>

class Emitter {
private:
    std::string outputFileName;
    std::string code;

public:
    Emitter(const std::string& fileName);
    void emit(const std::string& code);
    void emitLine(const std::string& code);
    void writeFile();
    std::string getCode() const; // New method to retrieve the generated code
};
