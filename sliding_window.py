'''
Algorithm:

1. Its sliding window problem
2. I will use set data structure to store each character and to check duplicate character
3. Use left = 0 and in for loop right will be len(s)  for r in range(len(s)):
4. update res with max between window_len and res as res = max(res, window_length)
'''


# sliding window, if we see same char twice within curr window, shift start position;
def lengthOfLongestSubstring(s: str) -> int:
    res = 0
    left = 0
    char_set = set()

    for right in range(len(s)):

        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        length = (right - left) + 1
        res = max(res, length)
    return res


def characterReplacement(s: str, k: int) -> int:

    left = 0
    res = 0
    char_map = {}

    for right in range (len(s)):

        char_map[s[right]] = 1 + char_map.get(s[right], 0)
        window = (right - left + 1) - max(char_map.values())
        while window > k:
            char_map[s[left]] -= 1
            left += 1

        res = max(res, (right - left + 1))

    return res


def main():

    print(characterReplacement("ABAB", 2))
    #print(lengthOfLongestSubstring("abccbabb"))


if __name__ == '__main__':
    main()
