# 🧩 Sudoku Solver & Generator

## 📌 Overview
A **Python command-line Sudoku program** that can **generate puzzles** of varying difficulty and **solve them automatically**.  

This project demonstrates **backtracking, recursion, object-oriented programming, and logical problem-solving** in a structured workflow similar to a data analysis pipeline.

---

## ⚙️ Workflow

### 1️⃣ System Recognition
**Goal:** Understand the problem domain and requirements.  
- **Domain:** Puzzle generation and solving (Sudoku 9x9).  
- **Objective:** Generate solvable puzzles of adjustable difficulty and solve them efficiently.  
- **Constraints:** Must respect Sudoku rules (unique numbers 1–9 per row, column, and 3x3 block).

---

### 2️⃣ Data Collection
**Goal:** Prepare the inputs for the system.  
- Gather the initial empty Sudoku board as a 9x9 grid.  
- Optionally accept **user input** for pre-filled numbers or difficulty selection.  

---

### 3️⃣ Data Cleaning
**Goal:** Ensure the board is valid and ready for processing.  
- Verify that initial board numbers (if any) do not violate Sudoku rules.  
- Fill missing cells during generation while maintaining validity.  

---

### 4️⃣ Exploratory Analysis
**Goal:** Analyze and process the data for insights.  
- Randomized backtracking algorithm fills the board completely.  
- **Check constraints** at every placement to avoid conflicts.  
- Determine cells to remove based on **difficulty level** (20–60 empty cells).  

---

### 5️⃣ Visualization
**Goal:** Present the puzzle in a readable and interactive way.  
- **Console display:** Nicely formatted 9x9 grid.  
- **Image output:** Save as PNG:
  - [Puzzle Image (`sudoku.png`)](./images/sudoku.png)  
  - [Solved Puzzle (`sudoku_solved.png`)](./images/sudoku_solved.png)  
- Optional enhancements: color-coded cells, bold 3x3 block separators.  

---

### 6️⃣ Insights / Solver Output
**Goal:** Produce actionable results.  
- Solve any valid puzzle automatically using **recursive backtracking**.  
- Output the **solved board** to console and optionally as a PNG image.  
- Demonstrates efficiency of algorithm and correctness of generation.  

---

## 🚀 Key Features

| Step | Feature | Technique / Concept |
|------|---------|-------------------|
| 1 | Sudoku Solver & Generator | CLI program that generates and solves puzzles automatically |
| 2 | Puzzle Initialization | 9x9 grid creation, user input handling |
| 3 | Board Validation | Check pre-filled cells for rule compliance |
| 4 | Puzzle Generation | Randomized backtracking, recursion, constraints |
| 5 | Display & Visualization | Console formatting, matplotlib PNG output |
| 6 | Solver | Recursive backtracking, solution verification |

---

## 🛠️ How to Run

```bash
python sudoku_solver_clean.py
