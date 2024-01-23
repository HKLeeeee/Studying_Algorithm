import sys

input = sys.stdin.readline

N = int(input())
money = list(map(int, input().split()))
total = int(input())
ans = -1


# x가 정수 상한액일때 전체 예산안에서 모두 배정이 가능한가
def determination(x):
    curr_total = 0
    global total
    max_ = -1
    for m in money:
        if m >= x:
            curr_total += x
            max_ = x
        else:
            curr_total += m
            max_ = max(max_, m)
    return curr_total <= total, max_


L, R = 0, max(money)
while L <= R:
    mid = (L + R) // 2
    deter, a = determination(mid)
    if deter:
        L = mid + 1
        ans = max(ans, a)
    else:
        R = mid - 1

print(ans)