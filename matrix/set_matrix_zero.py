from typing import List


def setZeroes(self, matrix: List[List[int]]) -> None:

    ROWS = len(matrix)
    COLS = len(matrix[0])
    set_zero = False

    for r in range(ROWS):
        for c in range(COLS):

            if matrix[r][c] == 0:
                matrix[0][c] = 0

                if r > 0:
                    matrix[r][0] = 0
                else:
                    set_zero = True


    for r in range(1, ROWS):
        for c in range(1, COLS):

            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0


    #


def zeros(self, matrix: List[List[int]])-> None:

    is_zero = False
    ROWS = len(matrix)
    COLS = len(matrix[0])

    for r in range(ROWS):
        for c in range(COLS):

            if matrix[r][c] == 0:
                matrix[0][c] = 0

            if r > 0:
                matrix[r][0] = 0
            else:
                is_zero = True

    for r in range(1, ROWS):
        for c in range(1, COLS):

            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[0][r] = 0

    if is_zero:
        for r in range(ROWS):
            matrix[r][0] = 0