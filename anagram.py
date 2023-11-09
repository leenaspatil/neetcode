import collections
from typing import List


def isAnagram(s: str, t: str) -> bool:
    s_map = {}
    t_map = {}

    for c in s:
        s_map[c] = s_map.get(c, 0) + 1
    for c in t:
        t_map[c] = t_map.get(c, 0) + 1
    return s_map == t_map


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    ans = collections.defaultdict(list)
    print(len(ans))
    for s in strs:
        count = [0] * 26
        for c in s:
            print("ord(c) : " + str(ord(c)) + " ord("") :" + str(ord("a")))
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)

    return ans.values()


def main():
    nums = [100, 4, 200, 1, 3, 2]

    s = "leena"
    t = "neela"
    #  print(isAnagram(s, t))
    s, t = "anagram", "nagaram"
    # print(isAnagram(s, t))
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))

def isAnagram1(s: str, t: str) -> bool:
    s_map = {}
    t_map = {}

    for c in s:
        s_map[c] = s_map.get(c, 0) + 1

    for c in t:
        t_map[c] = t_map.get(c, 0) + 1

    return s_map == t_map
if __name__ == '__main__':
    main()


count = [0] * 26

for c in str:
    count[ord()]