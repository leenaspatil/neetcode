import heapq


def findKthLargest(nums, k):

    heap = []

    for n in nums:
        heapq.heappush(heap,n)
        if len(heap) > k :
            heapq.heappop(heap)

    return heap[0]
