import sys
input = sys.stdin.readline
N, M = map(int, input().split())
budget = [int(input()) for _ in range(N)]
L, R = max(budget), 1000000000

def determination(k):
    cnt, s = 1, 0
    for b in budget:
        if s + b <= k:
            s += b
        else:
            cnt += 1
            s = b
    return cnt <= M

res = 0
while L <= R:
    mid = (L + R) // 2
    if determination(mid):
        res = mid
        R = mid - 1
    else:
        L = mid + 1
print(res)
