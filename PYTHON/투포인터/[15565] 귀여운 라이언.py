import sys

input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))

L, R = 0, 0
curr_cnt = 0
min_len = N + 1
while L < N:
    while R < N and curr_cnt < K:
        if a[R] == 1:
            curr_cnt += 1
        R += 1

    if curr_cnt >= K:
        min_len = min(min_len, R-L)

    if a[L] == 1:
        curr_cnt -= 1
    L += 1

if min_len == N + 1:
    min_len = -1
print(min_len)
