from typing import List


def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    res = []
    left, right = 0, len(matrix)
    top, bottom = 0, len(matrix[0])

    while left < right and top < bottom:

        # from left to right (top row)

        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1
        # from top to bottom (right row)
        for i in range(top, bottom):
            res.append(matrix[i][right])
        right -= 1
        #....check condition again
        if not (left < right and top < bottom) :
            break
        # from left to right (bottom row)

        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i ])

        # from bottom to top (left row)

        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        return res