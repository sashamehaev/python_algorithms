import sys

n = int(sys.stdin.readline().rstrip())
arr = sys.stdin.readline().rstrip().split()
arr = [int(item) for item in arr]

left = 0
left_arr = []
right_arr = []
count = 0
for i in range(1, n):
    left_arr = arr[left:i]
    right_arr = arr[i: n]
    if max(left_arr) < min(right_arr):
        left = i
        count += 1
    if i == n - 1:
        count += 1
print(count)
