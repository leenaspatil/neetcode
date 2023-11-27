import collections


def longest(s:str) -> int:

    left = 0
    char_count = set()
    res = 0

    for right in range(len(s)):

        if s[right] in char_count:
            char_count.remove(s[left])
            left += 1
        char_count.add(s[right])
        res = max(res, right - left + 1)

    return res



def main():
    print(longest("ABAB"))
    nums = [1,2,3]
    res = nums * 2
    print(nums)
    print(res)


if __name__ == '__main__':
    main()
