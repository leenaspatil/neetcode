

def fibonacci(n:  int) -> int:

    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print(fibonacci(4))


if __name__ == '__main__':
    main()