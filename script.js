import { solve_sudoku } from "./sudokuSolver.js";
import { predefinedSudoku } from "./predefinedSudoku.js";

const SUDOKU_SIZE = 9;
let sudoku = Array.from({ length: SUDOKU_SIZE }, () =>
    Array(SUDOKU_SIZE).fill(0)
);

const cells = Array.from({ length: SUDOKU_SIZE }, () => Array(SUDOKU_SIZE));

//Get query selector for the sudoku class
const sudokuBoard = document.querySelector(".sudoku");
const solveButton = document.querySelector("#solve_btn");
const loadButton = document.querySelector("#load_btn");
const resetButton = document.querySelector("#reset_btn");

//Event Listeners for the buttons
solveButton.addEventListener("click", solveButtonPressed);
loadButton.addEventListener("click", () => drawBoard(predefinedSudoku));
resetButton.addEventListener("click", resetBoard);

//Solve button
function solveButtonPressed() {
    console.log("Solving Sudoku!");
    sudoku = loadFromBoard();
    sudoku = solve_sudoku(sudoku, true);
    drawBoard(sudoku);

    /*
    solveSudokuAPI(sudoku).then((solvedSudoku) => {
        if (solvedSudoku) {
            drawBoard((sudoku = solvedSudoku));
        }
    });*/
}
// Reset board
function resetBoard() {
    for (let i = 0; i < SUDOKU_SIZE; i++) {
        for (let j = 0; j < SUDOKU_SIZE; j++) {
            cells[i][j].innerHTML = "";
        }
    }
}
//Get the board from the page and load it into the sudoku array
function loadFromBoard() {
    for (let i = 0; i < SUDOKU_SIZE; i++) {
        for (let j = 0; j < SUDOKU_SIZE; j++) {
            if (cells[i][j].innerHTML === "") {
                sudoku[i][j] = 0;
            } else {
                sudoku[i][j] = parseInt(cells[i][j].innerHTML);
            }
        }
    }
    return sudoku;
}

//----------------------------------------------------------------------------

//Activate cells by click
let activated = false;
for (let i = 0; i < SUDOKU_SIZE; i++) {
    for (let j = 0; j < SUDOKU_SIZE; j++) {
        cells[i][j] = document.getElementById(`c_${i}-${j}`);
        cells[i][j].addEventListener("click", () => {
            if (activated) {
                document
                    .querySelector(".activated-cell")
                    .classList.toggle("activated-cell");
            }

            cells[i][j].classList.toggle("activated-cell");
            activated = true;
        });
    }
}

//Deactivate cell by clicking cell or outside cell
document.addEventListener("click", (event) => {
    if (!sudokuBoard.contains(event.target)) {
        if (activated) {
            document
                .querySelector(".activated-cell")
                .classList.toggle("activated-cell");
        }
        activated = false;
    }
});

//Keylistener for keyboard presses
document.addEventListener("keydown", (event) => {
    if (activated) {
        for (let i = 1; i <= 9; i++) {
            if (event.key === String(i)) {
                document.querySelector(".activated-cell").innerHTML = i;
            }
        }
        if (event.key === "Backspace" || event.key === "Delete") {
            document.querySelector(".activated-cell").innerHTML = "";
        }
    }

    console.log(`Key pressed: ${event.key}`);
});

//Fill board with the content of the sudoku array
function drawBoard(sudoku) {
    for (let i = 0; i < SUDOKU_SIZE; i++) {
        for (let j = 0; j < SUDOKU_SIZE; j++) {
            if (sudoku[i][j] === 0) {
                cells[i][j].innerHTML = "";
            } else {
                cells[i][j].innerHTML = sudoku[i][j];
            }
        }
    }
}

//---------------------------------------------------------------------------

//CALL THE PYTHON BACKEND TO SOLVE THE SUDOKU (Used with earlier version)
/*async function solveSudokuAPI(sudoku) {
    try {
        const response = await fetch("http://127.0.0.1:5000/solve-sudoku", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ sudoku }),
        });

        if (!response.ok) {
            throw new Error("Failed to communicate with Python backend");
        }

        const data = await response.json();
        console.log("Returned Sudoku:", data.result);
        return data.result;
    } catch (error) {
        console.error("Error processing matrix:", error);
        return null;
    }
}*/

//---------------------------------------------------------------------------
