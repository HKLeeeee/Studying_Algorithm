import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = sorted(list(map(int, input().split())))

def get_amount(h):
    amount = 0
    for i in range(N - 1, -1, -1):
        if trees[i] <= h:
            break
        amount += (trees[i] - h)
    return amount


l = 0
r = trees[-1] + 1
res = l
while l <= r:
    mid = (l + r) // 2
    if get_amount(mid) >= M:
        l = mid + 1
        res = mid
    else:
        r = mid - 1

print(res)