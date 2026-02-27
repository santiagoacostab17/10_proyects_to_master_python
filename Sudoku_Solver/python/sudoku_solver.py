# sudoku_solver_clean.py
import random
import matplotlib.pyplot as plt
import os

# ---------------------
# Board Generator
# ---------------------
def generate_empty_board():
    return [[0]*9 for _ in range(9)]

def print_board(board):
    for i, row in enumerate(board):
        print(" ".join(str(num) if num != 0 else "_" for num in row[:3]) + " | " +
              " ".join(str(num) if num != 0 else "_" for num in row[3:6]) + " | " +
              " ".join(str(num) if num != 0 else "_" for num in row[6:]))
        if i in [2,5]:
            print("-"*21)

# ---------------------
# Sudoku Solver
# ---------------------
def is_valid(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[r][col] for r in range(9)]:
        return False
    start_row, start_col = 3*(row//3), 3*(col//3)
    for r in range(start_row, start_row+3):
        for c in range(start_col, start_col+3):
            if board[r][c] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col]==0:
                for num in range(1,10):
                    if is_valid(board,row,col,num):
                        board[row][col]=num
                        if solve(board):
                            return True
                        board[row][col]=0
                return False
    return True

# ---------------------
# Sudoku Generator
# ---------------------
def fill_board(board):
    numbers = list(range(1,10))
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid(board,i,j,num):
                        board[i][j]=num
                        if fill_board(board):
                            return True
                        board[i][j]=0
                return False
    return True

def remove_numbers(board, n=40):
    cells = [(r,c) for r in range(9) for c in range(9)]
    for row,col in random.sample(cells, n):
        board[row][col]=0

# ---------------------
# Visualization
# ---------------------
def show_board(board, filename="images/sudoku.png"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    fig, ax = plt.subplots(figsize=(6,6))
    ax.set_xlim(0,9)
    ax.set_ylim(0,9)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.invert_yaxis()

    # Draw grid lines
    for i in range(10):
        lw = 2 if i%3==0 else 1
        ax.plot([0,9],[i,i], color='black', lw=lw)
        ax.plot([i,i],[0,9], color='black', lw=lw)

    # Draw numbers
    for r in range(9):
        for c in range(9):
            if board[r][c]!=0:
                ax.text(c+0.5, r+0.5, str(board[r][c]),
                        ha='center', va='center', fontsize=18)

    plt.savefig(filename, bbox_inches='tight')
    plt.show()
    plt.close()

# ---------------------
# Main
# ---------------------
def main():
    board = generate_empty_board()
    fill_board(board)

    while True:
        try:
            n = int(input("Enter number of cells to remove (20-60): "))
            if 20 <= n <= 60:
                break
            print("Number must be 20-60.")
        except ValueError:
            print("Enter a valid number.")

    remove_numbers(board, n)
    print("\n🧩 Sudoku Puzzle")
    print_board(board)
    show_board(board)

    if input("Do you want to solve it? (y/n): ").lower()=='y':
        solve(board)
        print("\n✅ Solved Sudoku")
        print_board(board)
        show_board(board, filename="images/sudoku_solved.png")

if __name__=="__main__":
    main()
