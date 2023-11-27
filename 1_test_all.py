import collections
import heapq

import math
from collections import deque
from heapq import *
from typing import List, Optional

'''class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = next'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insertion(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        j = i - 1
        while j > 0 and nums[j + 1] < nums[j]:
            temp = nums[j - 1]
            nums[j - 1] = nums[j - 1]
            nums[j - 1] = temp
            j -= 1


def main():
    stu, sand = [1, 1, 1, 0, 0, 1], [1, 3, 3, 3, 2, 2, 1, 1]
    nums = [-1, 0, 1, 2, -1, -4]


if __name__ == '__main__':
    main()
