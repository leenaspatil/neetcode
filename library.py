from typing import List


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
