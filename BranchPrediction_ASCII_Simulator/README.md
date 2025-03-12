<!-- Replace the image link below with your own banner -->
# 🧠 Branch Predictor Simulator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python" alt="Python 3.8+"/>
  <img src="https://img.shields.io/badge/Simulator-ASCII%20%2F%20CLI-success?style=flat-square" alt="CLI"/>
</p>

<p align="center">
  <b>A configurable simulator for evaluating branch prediction algorithms: Smith n_BIT, Bimodal, GShare, and Hybrid predictors.</b>
</p>


---

## 🚀 Overview

**Branch Predictor Simulator** is a Python-based tool for analyzing branch prediction strategies used in modern CPU architectures. It:
- Simulates 4 prediction algorithms: **Bimodal**, **GShare**, **Hybrid** and **Smith n_BIT**
- Processes trace files to evaluate prediction accuracy
- Displays real-time statistics including misprediction rates and predictor table states
- Features an ASCII-based CLI interface for visualization

---

## 📚 What is Branch Prediction?

Branch prediction is a critical technique in computer architecture that **reduces pipeline stalls** by guessing the outcome of conditional branches (e.g., "if" statements). Modern CPUs use predictors to:
- Improve instruction throughput
- Minimize pipeline bubbles
- Boost overall performance

### Types Implemented:
1. **Bimodal Predictor**  
   Uses a pattern history table with 2-bit saturating counters. Best for simple branch patterns.

2. **GShare Predictor**  
   Combines global branch history (GBHR) with XOR-based indexing. Effective for correlated branches.

3. **Hybrid Predictor**  
   Merges Bimodal and GShare predictions using a "chooser table" for optimal accuracy.

4. **Smith N-bit Predictor**  
   Utilizes an N-bit counter for each branch, incremented or decremented based on outcomes, for simple and fast predictions.

---

## ⚙️ Features

- Real-time interactive ASCII visualization of predictor tables
  ![ASCII Simulator Demo](BranchPrediction_ASCII_Simulator/ezgif.com-video-to-gif-converter.gif)

  4 Branch Prediction simulators display how the Counter Tables and performance metrics change in real time. 

## 🛠️ Project Structure
```plaintext
.
├── BimodalBP.py        # Bimodal predictor
├── GShare.py           # GShare predictor
├── HybridBP.py         # Hybrid predictor
├── ascii_simulation.py # CLI visualization
├── nBIT.py             # 2-bit counter logic
├── traces/             # Branch trace files
├── validation_runs/    # Test configurations
└── sim                 # Main launcher
```
# ✅ Conclusion
Thanks for checking out this project!

