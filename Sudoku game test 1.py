# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 19:34:42 2023

@author: Sam
"""

import random

# Generate empty board
def generate_board():
    board = [[0 for i in range(9)] for j in range(9)]
    return board

# Check if a number is valid for a given row, column, and square
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
        if board[i][col] == num:
            return False
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if board[i][j] == num:
                return False
    return True

# Solve the Sudoku puzzle using backtracking
def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# Remove some numbers from the solved board to generate the game board
def generate_game_board(board, difficulty):
    num_cells = 81 - difficulty
    while num_cells > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            num_cells -= 1

# Print the board in a user-friendly format
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Allow the user to input numbers to solve the Sudoku game
def input_numbers(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                while True:
                    try:
                        num = int(input("Enter a number between 1 and 9 for row " + str(i+1) + " column " + str(j+1) + ": "))
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            break
                        else:
                            print("Invalid number! Try again.")
                    except ValueError:
                        print("Invalid input! Try again.")

# Generate the Sudoku game board
board = generate_board()
solve(board)
generate_game_board(board, 50)

# Print the game board
print("Sudoku Game:")
print_board(board)

# Allow the user to input numbers to solve the Sudoku game
input_numbers(board)

# Print the solved board
print("Solved Sudoku Game:")
print_board(board)
