from typing import List
'''
1. its heap problem
2. I will use dict to store counts
3. Also using list of list I will add in list of list the most freq element with that number value e.g [1,1,2,2,2,2,1,1,3,3] freq[4]->[1,2], freq[2]->[3]
4. loop in reverse order to get max count till k 
'''


def topKFrequent(nums: List[int], k: int) -> List[int]:
    res = []
    freq = [[] for i in range (len(nums) + 1)]
    count = {}

    for n in nums:
        count[n] = 1 + count.get(n,0)
    # add element in freq from dict

    for key, val in count:
        freq[val].append(key)

    for i in range(len(nums) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
        if len(res) == k:
            return res



