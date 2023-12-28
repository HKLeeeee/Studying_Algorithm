import sys

input = sys.stdin.readline
N = int(input())  # 2 이상 100,000 이하
nums = sorted(list(map(int, input().split())))  # 정렬 O(NlogN)
L, R = 0, N - 1
v1, v2 = 0, 0
min_ = 1 << 31  # 가능한 두 용액의 합의 최대 1999999999

while L < R:
    s = nums[L] + nums[R]
    if abs(s) < min_:
        min_ = abs(s)
        v1, v2 = nums[L], nums[R]
    if s == 0:
        v1, v2 = nums[L], nums[R]
        break

    if s < 0:
        L += 1
    else:
        R -= 1
print(v1, v2)
print(1 << 31 )

