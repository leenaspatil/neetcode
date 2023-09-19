from typing import List


def encode(strs: List[str]) -> str:
    res = ""

    for s in strs:
        res = res + str(len(s)) + "#" + s
    return res


def decode(s: str) -> List[str]:
    start = 0
    res = []

    while start < len(s):
        end = start

        while s[end] != "#":
            end += 1
        length = int(s[start:end])
        res.append(s[end + 1:end + length + 1])
        start = end + length + 1

    return res


def main():

    str1 = encode(["leena","sunil"])
    print(str1)
    print(decode(str1))


if __name__ == '__main__':
    main()
