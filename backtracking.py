from typing import List


def exist(board: List[List[str]], word: str) -> bool:  # its backtracking solution
    ROWS = len(board)
    COLUMNS = len(board[0])
    visited = set()

    def dfs(row: int, col: int, index: int) -> bool:

        if index == len(word):
            return True

        if row < 0 or row >= ROWS or col < 0 or col >= COLUMNS:
            return False

        if board[col][row] != word[index]:
            return False

        if (row, col) in visited:
            return False

        visited.add(row, col)

        result = {
            dfs(row + 1, col, index + 1) or
            dfs(row - 1, col, index + 1) or
            dfs(row, col + 1, index + 1) or
            dfs(row, col + 1, index + 1)
        }

        return result

        for r in range(ROWS):
            for c in range(COLUMNS):
                if dfs(r , c, 0):
                    return True

        return False