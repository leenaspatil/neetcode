from typing import List


def two_sum(nums: List[int], target: int) -> int:
    prev_map = {}

    for i, n in enumerate(nums):
        diff = target - n
        if target - n in prev_map:
            return [prev_map[diff], i]

        prev_map[n] = i


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    res = []
    num_count_map = {}
    freq = [[] for i in range(len(nums))]
#    [1, 1, 2, 2, 2, 2, 1, 1, 3, 3]
    for num in nums:
        num_count_map[num] = 1 + num_count_map.get(num, 0)
#        1 : 4  2:  4, 3: 2
    for key, value in num_count_map.items():
        freq[value] = freq[value].append(key)

    for i in range(len(nums) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
        if len(res) == k:
            return res


def rotate(self, matrix: List[List[int]]) -> None:
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            # save top left

            top_left = matrix[top][left + i]

            # move bottom left into top left
            matrix[top][left + i] = matrix[bottom - i][left]
            # move bottom right into bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # move top right into bottom right
            matrix[bottom][right - i] = matrix[top + i][right]
            # place topLeft variable val to top right
            matrix[top + i][right] = top_left
        left += 1
        right -= 1


def valid_palin(self, s: str) -> bool:

    left, right = 0, len(s) - 1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
           right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True


def exist(self, board: List[List[str]], word: str) -> bool: # its backtracking solution

    ROWS, COLUMNS = len(board), len(board[0])
    visited_index =  set()

    def dfs(row: int, col: int, index: int) -> bool:

        if index == len(word):
            return True

        if row < 0 or row >= ROWS or col < 0 or col >= COLUMNS:
            return False

        if (row, col) in visited_index:
            return False

        visited_index.add((row, col))

        result = (

            dfs(row, col + 1, index + 1) or
            dfs(row, col - 1, index + 1) or
            dfs(row + 1, col, index + 1) or
            dfs(row - 1, col, index + 1)
        )
        visited_index.remove((row, col))

        return result

    for r in range(ROWS):
        for c in range(COLUMNS):
            if dfs(r, c, 0):
                return True
    return False


def hamming_weight(n: int) -> int:

    res = 0
    while n:
        res += n % 2
        n = n >> 1
    return res


def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])

    for i in range(1,len(intervals)):

        if intervals[i][0] < intervals[i-1][1]:
            return False

    """
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda meeting: meeting[0])

        for index in range(1,len(intervals)):

            # if start time of next meeting is less that end time of previous meeting means they are overlapping

            if intervals[index][0] < intervals[index-1][1]:
                return False
        return True
    """