import sys

input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
L, R = 0, 0
curr_sum = 0
cnt = 0

while L < N:
    while curr_sum < S and R < N:
        curr_sum += nums[R]
        R += 1

    if curr_sum == S:
        cnt += 1

    curr_sum -= nums[L]
    L += 1
print(cnt)
