# -*- coding: utf-8 -*-

"""

Created on Tue Mar 28 19:34:42 2023



@author: Sam

"""


From typing import List

import random



# Generate empty board

def generate_board() -> List[List[int]]:
    return [[0] * 9 for _ in range(9)]



# Check if a number is valid for a given row, column, and square

def is_valid(board: List[List[int]], row: int, col: int, num: int) -> bool:
    row_vals = set(board[row])
    col_vals = {board[i][col] for i in range(9)}
    square_vals = {board[i][j] for i in range(row // 3 * 3, (row // 3 + 1) * 3) for j in range(col // 3 * 3, (col // 3 + 1) * 3)}
    return num not in row_vals and num not in col_vals and num not in square_vals



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

def main() -> None:
    board = generate_board()
    solve(board)
    generate_game_board(board, 50)
    print("Sudoku Game:")
    print_board(board)
    input_numbers(board)
    print("Solved Sudoku Game:")
    print_board(board)

