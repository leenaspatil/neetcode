def count_bits(n: int) -> int:
    count = 0
    while n:

        count += n % 2
        n = n >> 1
    return count


def main():
    print(count_bits(3))


if __name__ == '__main__':
    main()