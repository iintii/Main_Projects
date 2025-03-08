<!-- 
  Replace the image link below with your own banner or an image you like! 
  For example, you can upload one to Imgur and link it here.
-->
# 🛠️ Compiler (From Scratch)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python&logoColor=white" alt="Python 3.10"/>
  <img src="https://img.shields.io/badge/Status-Complete-success?style=flat-square"/>
  <img src="https://img.shields.io/badge/Language-C%20Output-important?style=flat-square&logo=c"/>
</p>

<p align="center">
  <b>A minimalist compiler that translates a custom scripting language into C code, built entirely from scratch in Python!</b>
</p>

---

## 🚀 Overview

**Teeny Tiny Compiler** is a straightforward yet powerful project demonstrating the fundamentals of **compiler construction**. It takes a custom language (with commands like `LET`, `WHILE`, `IF`, `PRINT`, etc.) and generates equivalent **C** code, ready to compile and run.

**Key components:**
- **Lexical Analysis** (`lex.py`)
- **Parsing & AST** (`parse.py`)
- **Code Emission** (`emit.py`)
- **Main Driver** (`main`) that orchestrates the entire process

---

## ⚙️ How It Works

1. **Lexer** reads and **tokenizes** the source file into recognizable symbols (e.g., `LET`, `IF`, `PRINT`, operators).
2. **Parser** performs **recursive descent** to check grammar validity and build a high-level structure.
3. **Emitter** transforms this structure into valid **C** code, saved as `out.c`.
4. **Compile** `out.c` using your favorite C compiler, and run the resulting binary.

---

## 🏗️ Project Structure

```plaintext
.
├── emit.py       # Emitter class that writes the final C code to out.c
├── lex.py        # Lexer: Tokenizes the source code
├── parse.py      # Parser: Implements grammar rules (recursive descent)
├── main          # Main driver script that pulls everything together
├── sample.src    # Example custom language source
└── out.c         # Generated C code after compilation
```
---

## ✅ Conclusion

Thank you for exploring this project!

