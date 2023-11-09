import collections
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    map = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in map:
            return [i, map.get(diff)]
        map[n] = i


def greet():
    print("hello world")


def longestConsecutive(nums: List[int]) -> int:
    num_set = set(nums)
    longest = 0

    for n in nums:

        if (n - 1) not in num_set:
            length = 1
            while (n + length) in num_set:
                length += 1
            longest = max(length, longest)
    return longest


def climbStairs(n):
    # edge cases
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 2

    dp = [0] * (n + 1)  # considering zero steps we need n+1 places
    print(dp)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    res = []
    while left < right and top < bottom:

        # get every ele in top row
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        # get every ele in right
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right -= 1

        if not (left < right and top < bottom):
            break
        # get every ele in bottom row
        for i in range(right - 1, left - 1, -1):
            res.append(matrix[bottom - 1][i])
        bottom -= 1

        # get every ele in left
        for i in range(bottom - 1, top - 1, -1):
            res.append(matrix[i][left])
        left += 1

    return res


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    list1 = collections.defaultdict(list)

    for s in str:

        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        list1[tuple(count)].append(s)

    return list1.values()


def productExceptSelf(nums: List[int]) -> List[int]:
    # solve the problem using prefix and sufix where initial prefix for first array num is 1
    # same way initial sufix for last num is 1

    # we will use 2 pass - one in- order and other is reverse order using new array values

    result = [1] * len(nums)
    prefix = 1
    for index in range(len(nums)):
        result[index] = prefix
        print(result)
        prefix = prefix * nums[index]

    suffix = 1
    for index in range(len(nums) - 1, -1, -1):
        result[index] = suffix * result[index]
        print(result)

        suffix = suffix * nums[index]
    return result


# list = [1,2,3,4]
# print(productExceptSelf([1,2,3,4]))

def exist(self, board: List[List[str]], word: str) -> bool:
    ROWS = len(board)
    COLS = len(board[0])
    visited = set()

    def dfs(row: int, col: int, index: int) -> bool:
        if index == len(word):
            return True

        if row < 0 or row >= ROWS or col < 0 or col >= COLS:
            return False
        if board[row][col] != word[index]:
            return False
        if (row, col) in visited:
            return False

        visited.add((row, col))

        result = (
                dfs(row + 1, col, index + 1) or
                dfs(row - 1, col, index + 1) or
                dfs(row, col + 1, index + 1) or
                dfs(row, col - 1, index + 1)
        )

        visited.remove((row, col))

        return result

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):  ## its backtracking solution
                return True
    return False
