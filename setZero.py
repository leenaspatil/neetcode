from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    ROWS = len(matrix)
    COLS = len(matrix[0])
    zero_row = False
    for row in range(ROWS):
        for col in range(COLS):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[row][col] == 0:
                matrix[0][col] = 0
                if row > 0:
                    matrix[row][0] = 0
                else:
                    zero_row = True
    print(f'After calculating first step {matrix}')

    # Iterate over the array once again and using the first row and first column, update the elements.

    for row in range(1, ROWS):
        for col in range(1, COLS):
            if matrix[0][col] == 0 or matrix[row][0] == 0:
                matrix[row][col] = 0
    print(f'After setting non-zero row, cols {matrix}')

    # See if the first row needs to be set to zero as well
    if matrix[0][0] == 0:
        for row in range(ROWS):
            matrix[row][0] = 0

    print(f'After processing zeroth row {matrix}')

    # See if the first column needs to be set to zero as well
    if zero_row:
        for col in range(COLS):
            matrix[0][col] = 0


def main():
    setZeroes([[1, 0, 1]])


if __name__ == '__main__':
    main()





