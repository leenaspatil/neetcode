from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    for i, n in enumerate(nums):

        if n > 0:
            break
        if i > 0 and n == nums[i - 1]:
            continue

        left, right = (i + 1), len(nums) - 1

        while left < right:

            sum = n + nums[left] + nums[right]

            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                res.append(sum)
                left += 1
                right -= 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

        return res
