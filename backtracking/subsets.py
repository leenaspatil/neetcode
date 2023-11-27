from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    subset = []

    def dfs(index: int):

        if index >= len(nums):
            i = 1
            res.append(subset.copy())
            print(res, i)
            i += 1
            return

        subset.append(nums[index])
        dfs(index + 1)
        subset.pop()
        dfs(index + 1)

    dfs(0)
    return res


def main():
    nums = [1, 2, 3]
    print(subsets(nums))


if __name__ == '__main__':
    main()
