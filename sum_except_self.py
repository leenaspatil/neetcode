from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
    prefix = 1
    res = [1] * len(nums)
    for i in range(nums):
        res[i] = prefix
        prefix *= nums[i]

    suffix = 1

    for i in range(len(nums) - 1, -1, -1):
        res[i] = suffix * res[i]
        suffix *= nums[i]

    return res
