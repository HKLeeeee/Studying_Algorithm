import sys
input = sys.stdin.readline
N, L = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(N)]
ans = 0

def check(r):
    slide = [False for _ in range(N)]
    for i in range(N - 1):
        if r[i] == r[i + 1]:
            continue
        if abs(r[i] - r[i + 1]) > 1:
            return False
        if r[i] > r[i + 1]:  # 내리막길
            height = r[i + 1]
            for j in range(i + 1, i + L + 1):
                if 0 <= j < N:
                    if slide[j]:
                        return False
                    if r[j] != height:
                        return False
                    slide[j] = True
                else:
                    return False
        else:  # 오르막길
            height = r[i]
            for j in range(i, i - L, -1):
                if 0 <= j < N:
                    if slide[j] :
                        return False
                    if r[j] != height:
                        return False
                    slide[j] = True
                else:
                    return False
    return True

for r in road:
    if check(r):
        ans += 1

for j in range(N):
    temp = []
    for i in range(N):
        temp.append(road[i][j])
    if check(temp):
        ans += 1

print(ans)
