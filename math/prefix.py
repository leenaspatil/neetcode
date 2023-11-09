from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:

    prefix = 1
    suffix = 1
    res = []
    for i in range(len(nums)):
        res[i] = prefix
        prefix = prefix * nums[i]

    for i in range(len(nums)-1, -1, -1):
        res[i] = suffix * res[i]
        suffix = suffix * nums[i]

    return res


def ware(nums: List[int]) -> int:

    max_area = 0

    left, right = 0, len(nums)

    while left < right:

        min_height =  min(nums[left] , nums[right])
        area = min_height * (right - left)
        max_area = max (max_area, area)

        if nums[left] < nums[right]:
            left += 1

        else:
            right -= 1

    return max_area