import sys


def main():
    soil_in_rover = sys.stdin.readline().rstrip().split()
    soil_in_rover = [int(item) for item in soil_in_rover]
    required_soil = int(sys.stdin.readline().rstrip())

    left = 0
    right = len(soil_in_rover) - 1
    index = 0
    while left <= right:
        mid = (left + right) // 2
        if soil_in_rover[mid - 1] < required_soil < soil_in_rover[mid]:
            index = mid
            break
        if soil_in_rover[right] < required_soil:
            index = right + 1
            break
        if soil_in_rover[mid] == required_soil:
            for i in range(mid + 1):
                if soil_in_rover[i] == required_soil:
                    index = i
                    break
            break
        if soil_in_rover[mid] < required_soil:
            left = mid + 1
        else:
            right = mid - 1
    print(index)


if __name__ == '__main__':
    main()
