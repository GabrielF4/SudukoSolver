#Coding challenge 7 (Sudoko solver)

import numpy as np

#Explanation of how subsquares work
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

#Convert from full scale coordinates to subsquare coordinates
def convert_to_sub_square(row, col):
    return (row//3, col//3)

#Control if the sudoku was solved
def check_if_solved(sudoku):
    for row in sudoku:
        for elem in row:
            if elem == 0:
                return False
            elif elem not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print("ERROR! Incorrect number in solution!")
                return False          
    return True

sudoku = np.array([[9, 8, 5, 4, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 3, 0, 0, 0, 0],
                    [1, 0, 6, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 5, 0, 0, 0, 0, 0],
                    [4, 0, 2, 0, 0, 9, 0, 0, 3],
                    [0, 9, 0, 0, 6, 3, 4, 0, 0],
                    [0, 6, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 3, 0, 6, 0, 0, 5],
                    [2, 0, 0, 0, 8, 0, 0, 0, 1]])

sudoku_easy = np.array([[5, 0, 0, 4, 6, 7, 3, 0, 9],
                    [9, 0, 3, 8, 1, 0, 4, 2, 7],
                    [1, 7, 4, 2, 0, 3, 0, 0, 0],
                    [2, 3, 1, 9, 7, 6, 8, 5, 4],
                    [8, 5, 7, 1, 2, 4, 0, 9, 0],
                    [4, 9, 6, 3, 0, 8, 1, 7, 2],
                    [0, 0, 0, 0, 8, 9, 2, 6, 0],
                    [7, 8, 2, 6, 4, 1, 0, 0, 5],
                    [0, 1, 0, 0, 0, 0, 7, 0, 8]])

#Temps and flags
sudoku_temp = sudoku
counter = 1
solutions_found = True
debug = False

print("\nSudoku to solve:")
print(f"\n{sudoku}\n")


while solutions_found:
    
    #Terminate program if stuck in loop
    if counter > 100:
        print("ERROR! Too many iterations!")
        exit()

    if debug:
        print(f"Iteration: {counter}...")

    solutions_found = False

    for row_index, row in enumerate(sudoku):
        for col_index, number in enumerate(row):

            #Trigger solution search if an empty square is found
            if number == 0:
                
                possible_solutions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                
                #Check available numbers in row
                for value in row:
                    if value in possible_solutions:
                        possible_solutions.remove(value)
                
                #Check available numbers in column
                for row_temp in sudoku:
                    if row_temp[col_index] in possible_solutions:
                        possible_solutions.remove(row_temp[col_index])
                
                #Calculate which subsquare the index is in
                sub_row, sub_col = convert_to_sub_square(row_index, col_index)
                
                #Check available numbers in subsquare
                for i in range(3):
                    for j in range(3):
                        temp = sudoku[sub_row * 3 + i, sub_col * 3 + j]
                        if temp in possible_solutions:
                            possible_solutions.remove(temp)

                #Check if found a solution
                if len(possible_solutions) == 1:
                    if debug:
                        print(f"Solution found on ({row_index}, {col_index}) Value: {possible_solutions[0]}")
                    sudoku_temp[row_index][col_index] = possible_solutions[0]
                solutions_found = True
                
                #Check if no possible values
                if len(possible_solutions) == 0:
                    print(f"ERROR: No valid solutions on ({row_index},{col_index})")
                    exit()
    
    #Control if sudoku is solved
    if not solutions_found:
        if debug:
            print("No more solutions found! Exiting software...")

        if check_if_solved(sudoku):
            print("Sudoku solved!")
        else:
            print("This sudoku could not be solved")

    #Update sudoku and counter
    sudoku = sudoku_temp
    counter += 1       

print(f"\n{sudoku}")