import sys


def main():
    string = sys.stdin.readline().rstrip()
    substring = []
    max_len = 0
    index = 0
    while index < len(string):
        if string[index] not in substring:
            substring.append(string[index])
        else:
            if len(substring) > max_len:
                max_len = len(substring)
            while string[index] in substring:
                substring.pop(0)
            substring.append(string[index])
        index += 1
    result = max(max_len, len(substring))

    print(result)


if __name__ == '__main__':
    main()
