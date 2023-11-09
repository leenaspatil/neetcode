import collections
from typing import List, Optional


'''class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = next'''


class ListNode:
    def __init__(self, val,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def reverse_bit(n:int) -> int:

    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res = res | (bit << (31 -i))
    return res


def duplicate(nums:List[int]) -> int:

    left = 0
    for right in range(len(nums)):

        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]

    return left + 1


def insertion_sort(nums:List[int]) -> None:

    for i in range(1,len(nums)):
        j = i - 1
        while nums[i] < nums[j]:

            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            j += 1
    print(nums)


def sum_3(nums:List[int]) -> List[List[int]]:
    res =[]
    for i in range(len(nums)):
        a = nums[i]

        if a > 0:
            break
        elif i > 0 and nums[i - 1] == nums[i]:
            continue
        else:
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum1 = a + nums[left] + nums[right]
                if sum1 > 0:
                    right -= 1
                elif sum1 < 0:
                    left += 1
                else:
                    res.append([a,nums[left],nums[right]])

                    while left > 0 and nums[left] == nums[left +  1]:
                        left += 1
        return  res




def main():
    print(duplicate([0,0,1,1,1,2,2,3,3,4]))


if __name__ == '__main__':
    main()
