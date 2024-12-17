import sys


def barometr(n, first, next):
    if n == 0 and first == 1:
        print(first)
        return
    if n == 0:
        print(first)
        return
    n -= 1
    barometr(n, next, first + next)


def main():
    first = 1
    next = 1
    generation = int(sys.stdin.readline().rstrip())
    barometr(generation, first, next)


if __name__ == '__main__':
    main()
