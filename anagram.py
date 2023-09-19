def isAnagram(s: str, t: str) -> bool:
    s_map = {}
    t_map = {}

    for c in s:
        s_map[c] = s_map.get(c, 0) + 1
    for c in t:
        t_map[c] = t_map.get(c, 0) + 1
    return s_map == t_map


def main():
    nums = [100, 4, 200, 1, 3, 2]
    print((nums))
    s = "leena"
    t = "neela"
    print(isAnagram(s, t))
    s, t = "anagram", "nagaram"
    print(isAnagram(s, t))


if __name__ == '__main__':
    main()
