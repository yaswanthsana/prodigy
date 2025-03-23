import tkinter as tk
from tkinter import messagebox

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def get_board():
    return [[int(entries[row][col].get() or 0) for col in range(9)] for row in range(9)]

def set_board(board):
    for row in range(9):
        for col in range(9):
            entries[row][col].delete(0, tk.END)
            entries[row][col].insert(0, str(board[row][col]))

def solve():
    board = get_board()
    if solve_sudoku(board):
        set_board(board)
        messagebox.showinfo("Success", "Sudoku Solved Successfully!")
    else:
        messagebox.showerror("Error", "No solution exists!")

def clear_board():
    for row in range(9):
        for col in range(9):
            entries[row][col].delete(0, tk.END)

root = tk.Tk()
root.title("Sudoku Solver")

entries = [[tk.Entry(root, width=3, font=('Arial', 16), justify='center') for _ in range(9)] for _ in range(9)]
for i in range(9):
    for j in range(9):
        entries[i][j].grid(row=i, column=j, padx=2, pady=2)

tk.Button(root, text="Solve", command=solve).grid(row=10, column=0, columnspan=4, pady=10)
tk.Button(root, text="Clear", command=clear_board).grid(row=10, column=5, columnspan=4, pady=10)

root.mainloop()
