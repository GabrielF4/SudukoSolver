const ROW_SIZE = 9;
const COL_SIZE = 9;

function convert_to_sub_square(row, col) {
    return [Math.floor(row / 3), Math.floor(col / 3)];
}

function check_if_solved(sudoku) {
    for (let i = 0; i < ROW_SIZE; i++) {
        for (let j = 0; j < COL_SIZE; j++) {
            if (sudoku[i][j] === 0) return false;
            else if (0 > sudoku[i][j] > 9) {
                console.error("ERROR! Incorrect number in solution!");
                return false;
            }
        }
    }
    return true;
}

function solve_sudoku(sudoku, debug = false) {
    //TODO: Fix weird referencing
    let sudoku_temp = sudoku;
    let counter = 1;
    let solutions_found = true;

    if (debug) {
        console.log("\nSudoku to solve:");
        console.log(`${sudoku}`);
    }

    while (solutions_found) {
        //Debug status
        if (debug) console.log(`Iteration: ${counter}...`);
        //Catching stuck loops
        if (counter > 404) {
            console.error("ERROR! Too many iterations!");
            break;
        }
        solutions_found = false;
        //Loop through the whole sudoku
        for (let row = 0; row < ROW_SIZE; row++) {
            for (let col = 0; col < COL_SIZE; col++) {
                //Trigger search for solution to square if square is 0
                if (sudoku[row][col] == 0) {
                    let possible_solutions = [1, 2, 3, 4, 5, 6, 7, 8, 9];
                    //Check which numbers exist on row
                    for (let k = 0; k < ROW_SIZE; k++) {
                        possible_solutions = possible_solutions.filter(
                            (x) => x !== sudoku[row][k]
                        );
                    }
                    //Check which numbers exist on col
                    for (let k = 0; k < COL_SIZE; k++) {
                        possible_solutions = possible_solutions.filter(
                            (x) => x !== sudoku[k][col]
                        );
                    }
                    //Check which numbers exists in sub-square
                    let [sub_row, sub_col] = convert_to_sub_square(row, col);
                    for (let k_row = 0; k_row < 3; k_row++) {
                        for (let k_col = 0; k_col < 3; k_col++) {
                            let temp =
                                sudoku[sub_row * 3 + k_row][
                                    sub_col * 3 + k_col
                                ];
                            possible_solutions = possible_solutions.filter(
                                (x) => x !== temp
                            );
                        }
                    }
                    //If only one posible number for a square then set that square to that number
                    if (possible_solutions.length === 1) {
                        if (debug) {
                            console.log(
                                `Solution found on (${row}, ${col}) with value (${possible_solutions[0]})`
                            );
                        }
                        sudoku_temp[row][col] = possible_solutions[0];
                        solutions_found = true;
                    }
                    //If an empty square has no possible solutions, something has gone wrong
                    if (possible_solutions.length == 0) {
                        console.error(
                            `ERROR: No valid solutions on (${row}, ${col})`
                        );
                        return sudoku;
                    }
                }
            }
        }
        //Exit program if whole sudoku iterated without any solutions found
        if (!solutions_found) {
            if (debug)
                console.log("No more solutions found! Exiting software...");

            if (check_if_solved(sudoku)) console.log("Sudoku solved!");
            else console.log("This sudoku could not be solved");
            break;
        }
        //Update sudoku and counter
        sudoku = sudoku_temp;
        counter++;
    }
    return sudoku;
}

export { solve_sudoku };
