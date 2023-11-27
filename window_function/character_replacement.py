import collections


def character_replacement(s:str,k :int)-> int:

    char_map = {}
    left = 0
    max_length = 0

    for right in range(len(s)):

        char_map[s[right]] = 1 + char_map.get(s[right], 0)

        print(f'Dict: ', char_map)
        while (right - left + 1) - max(char_map.values()) > k:
            char_map[s[left]] -= 1
            left += 1
            print(f' After: ', char_map)
        length = (right - left) + 1
        max_length = max(length, max_length)
    return max_length


def main():
    character_replacement("AAABAB", 2)


if __name__ == '__main__':
    main()
