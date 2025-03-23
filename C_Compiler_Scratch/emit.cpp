#include "emit.h"
#include <iostream>

Emitter::Emitter(const std::string& fileName) : outputFileName(fileName), code("") {
}

void Emitter::emit(const std::string& code) {
    this->code += code;
}

void Emitter::emitLine(const std::string& code) {
    this->code += code + "\n";
}

void Emitter::writeFile() {
    std::ofstream outFile(outputFileName);
    if (!outFile) {
        std::cerr << "Error: Could not open output file " << outputFileName << std::endl;
        exit(1);
    }
    outFile << code;
    outFile.close();
}

std::string Emitter::getCode() const {
    return code;
}
