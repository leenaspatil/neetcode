import collections
from typing import List, Optional


def bucket_sort(nums: List[int]) -> List[int]:
    count = [0, 0, 0]

    for n in nums:
        count[n] += 1
    i = 0
    for n in range(len(count)):
        for j in range(count[n]):
            nums[i] = n
            i += 1

    return nums
