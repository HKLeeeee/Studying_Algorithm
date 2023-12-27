import sys
input = sys.stdin.readline

N, C = map(int, input().split())
home = sorted([int(input()) for _ in range(N)])


def determination(D):
    # D만큼의 거리 차이를 두고 C개 만큼의 공유기를 설치할 수 있는가?
    select = home[0]  # Greedy 하게 선택
    cnt = 1
    global N, C
    for i in range(1, N):
        if home[i] - select >= D:
            cnt += 1
            select = home[i]
        if cnt >= C:
            return True
    return False


L, R = 0, home[-1]
res = -1
while L <= R:
    mid = (L + R) // 2
    if determination(mid):
        res = mid
        L = mid + 1
    else:
        R = mid - 1

print(res)
