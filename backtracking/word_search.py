# This is a recursive function that starts at particular row, column and index of character
def dfs(row: int, column: int, index: int) -> bool:
    if index == len(word):
        return True

    if row < 0 or row >= ROWS or column < 0 or column >= COLS:
        return False
    if board[row][column] != word[index]:
        return False
    if (row, column) in visited_index:
        return False

    visited_index.add((row, column))

    result = (
            dfs(row + 1, column, index + 1) or
            dfs(row - 1, column, index + 1) or
            dfs(row, column + 1, index + 1) or
            dfs(row, column - 1, index + 1)
    )
    visited_index.remove((row, column))

    return result