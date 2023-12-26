N = int(input())
A = list(map(int, input().split()))
A = [(i, x) for i, x in enumerate(A)]
B = sorted(A, key=lambda x: x[1])

P = [-1 for _ in range(N)]

for i in range(N):
    P[B[i][0]] = i

print(*P)
