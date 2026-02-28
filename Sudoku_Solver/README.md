# 🧩 Sudoku Solver & Generator

## 📌 Overview
A **Python command-line Sudoku program** that can **generate puzzles** of varying difficulty and **solve them automatically**.  

Designed for **students, Python enthusiasts, and algorithm learners**, it demonstrates **backtracking, recursion, and object-oriented programming** while providing a fully functional puzzle solver and generator.

---

## ⚙️ Features

- Generate **valid Sudoku puzzles** of different difficulty levels  
- Solve puzzles automatically using a **backtracking algorithm**  
- Adjustable **difficulty**: easy, medium, hard (based on number of empty cells)  
- **Interactive CLI** for manual input of puzzles  
- **Visualize puzzles** as PNG images  
- Clean, modular, **readable Python code** suitable for learning and modification  

---

## 🛠️ How It Works

1. **Puzzle Generation**  
   - Randomly generate a complete Sudoku board.  
   - Remove numbers based on the selected difficulty level to create a solvable puzzle.

2. **Puzzle Solving (`solve`)**  
   - Uses **backtracking recursion** to fill empty cells.  
   - Ensures the puzzle is solved according to Sudoku rules.  

3. **Visualization**  
   - Optionally save the puzzle as a **PNG image** for reference or sharing.  

---

## 🚀 Usage

1. Run the script:  
```bash
python sudoku_solver.py
