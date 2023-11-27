import collections
import heapq


def findKthLargest(s, k):
    count = collections.defaultdict(int)
    for c in s:
        count[c] += 1

    heap = []
    for item in count.items():
        heapq.heappush(heap, item[1], item[0])

    res = ''
    while heap:
        key, val = heapq.heappop(heap)
        res += key * val
    return res[::-1]
