from typing import List


def merge_sortArray(nums: List[int], s: int, e: int) -> List[int]:
    if (e - s + 1) <= 1:
        return nums

    m = (s + e) // 2

    merge_sortArray(nums, s, m)
    merge_sortArray(nums, m + 1, e)

    merge(nums, s, m, e)


def merge(arr, s, m, e):
    L = arr[s: m + 1]
    R = arr[m + 1: e + 1]

    i = 0
    j = 0
    k = s  # index for array

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
