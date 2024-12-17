import sys


def main():
    numbers_list = sys.stdin.readline().rstrip().split()
    numbers_list = [int(number) for number in numbers_list]
    result = []
    for number in numbers_list:
        counter = 0
        for i in range(len(numbers_list)):
            if number > numbers_list[i]:
                counter += 1
        result.append(counter)

    result = [str(number) for number in result]
    print(' '.join(result))


if __name__ == '__main__':
    main()
