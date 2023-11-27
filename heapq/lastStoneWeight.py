import heapq
from typing import List



def lastStoneWeight(stones: List[int]) -> int:

    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:

        first = heapq.heappop(stones)
        second = heapq.heappop(stones)

        if second > first:
            heapq.heappush(stones, first - second)

    return 0 if len(stones) < 1 else abs(stones[0])


def main():
    nums = [2, 7, 4, 1, 8, 1]
    print(lastStoneWeight(nums))


if __name__ == '__main__':
    main()
