import sys


def josephus(n, k):
    if n == 0:
        return 0
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1


def main():
    players_num = int(sys.stdin.readline().rstrip())
    tact = int(sys.stdin.readline().rstrip())
    print(josephus(players_num, tact))


if __name__ == '__main__':
    main()
