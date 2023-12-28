import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()
L, R = 0, 0
min_sub = 1 << 31
curr_sub = 0

while L < N:
    while R < N - 1 and curr_sub < M:
        curr_sub = nums[R] - nums[L]
        R += 1

    if curr_sub >= M:
        min_sub = min(min_sub, curr_sub)

    curr_sub = nums[R] - nums[L]
    L += 1

print(min_sub)
