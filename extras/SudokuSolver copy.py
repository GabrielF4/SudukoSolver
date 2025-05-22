#Coding challenge 7 (Sudoko solver)

import numpy as np

"""
Each sub squared is marked like this:

(0, 0) (0, 1) (0, 2)
(1, 0) (1, 1) (1, 2)
(2, 0) (2, 1) (2, 2)

To get the subsquare by matrix-cordinates you use subsquare = (row // 3, col // 3)

To get each cordinate in subsquare you use:

for i in range(3)
    for j in range(3)
        (sub_row * 3 + i, sub_col * 3 + j)

"""
def convert_to_sub_square(row, col):
    return (row//3, col//3)

sudoku = np.array([[9, 8, 5, 4, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 3, 0, 0, 0, 0],
                    [1, 0, 6, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 5, 0, 0, 0, 0, 0],
                    [4, 0, 2, 0, 0, 9, 0, 0, 3],
                    [0, 9, 0, 0, 6, 3, 4, 0, 0],
                    [0, 6, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 3, 0, 6, 0, 0, 5],
                    [2, 0, 0, 0, 8, 0, 0, 0, 1]])

sudoku2 = np.array([[5, 0, 0, 4, 6, 7, 3, 0, 9],
                    [9, 0, 3, 8, 1, 0, 4, 2, 7],
                    [1, 7, 4, 2, 0, 3, 0, 0, 0],
                    [2, 3, 1, 9, 7, 6, 8, 5, 4],
                    [8, 5, 7, 1, 2, 4, 0, 9, 0],
                    [4, 9, 6, 3, 0, 8, 1, 7, 2],
                    [0, 0, 0, 0, 8, 9, 2, 6, 0],
                    [7, 8, 2, 6, 4, 1, 0, 0, 5],
                    [0, 1, 0, 0, 0, 0, 7, 0, 8]])

sudoku_temp = sudoku2

sub_row_test, sub_col_test = (2, 1)

print("Subsquare Test: ")
for i in range(3):
    for j in range(3):
        temp = sudoku2[sub_row_test * 3 + i, sub_col_test * 3 + j]
        print(temp, end=" ")
    print()

print(f"The sudoku to solve: {sudoku2}")

counter = 100
run = True

while counter > 0 and run:
    run = False
    for row_index, row in enumerate(sudoku2):
        for col_index, number in enumerate(row):
            if number == 0:
                possible_solutions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                #Compare to row
                for value in row:
                    if value in possible_solutions:
                        possible_solutions.remove(value)
                #Compare to col
                for row_temp in sudoku2:
                    if row_temp[col_index] in possible_solutions:
                        print(row_temp[col_index])
                        possible_solutions.remove(row_temp[col_index])
                #Compare to subsquare
                
                #Figure out what subsquare you are in
                sub_row, sub_col = convert_to_sub_square(row_index, col_index)
                #Get numbers in same sub_square
                for i in range(3):
                    for j in range(3):
                        temp = sudoku2[sub_row * 3 + i, sub_col * 3 + j]
                        if temp in possible_solutions:
                            possible_solutions.remove(temp)

                #If there is only one possible solution then change the value

                #Check for squares with a solution
                if len(possible_solutions) == 1:
                    print(f"Row: {row_index}, Col: {col_index}, Value: {possible_solutions[0]}")
                    sudoku_temp[row_index][col_index] = possible_solutions[0]
                run = True
                
                #Check for squares without solution
                if len(possible_solutions) == 0:
                    print(f"ERROR: No valid solutions on ({row_index},{col_index})")
                    exit()
    sudoku2 = sudoku_temp
    counter -= 1         


print(f"The solved sudoku: {sudoku2}")