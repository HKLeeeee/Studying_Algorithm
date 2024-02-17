import sys
input = sys.stdin.readline

N = int(input())
X_A = []
total = 0
for _ in range(N):
    x, a = map(int, input().split())
    X_A.append((x, a))
    total += a
X_A.sort(key=lambda x: x[0])

cnt = 0
for (x, a) in X_A:
    cnt += a
    if cnt * 2 >= total:
        print(x)
        break
