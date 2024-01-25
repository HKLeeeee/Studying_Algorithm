import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

L, R = 0, N * N
res = 0


def determination(n):
    ## n보다 작은 수가 k개 이상인가
    cnt = 0
    for i in range(1, N + 1):
        if i * N < n:
            cnt += N
        else:
            cnt += n // i
    return cnt >= K


while L <= R:
    mid = (L + R) // 2
    if determination(mid):
        res = mid
        R = mid - 1
    else:
        L = mid + 1

print(res)
