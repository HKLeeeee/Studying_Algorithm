import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

D = [[0] * (N + 1) for _ in range(N + 1)]


def bfs(n):
    q = deque()
    q.append((n, 0))
    while q:
        node, dist = q.popleft()
        for nn in adj_list[node]:
            if D[n][nn] == 0 and nn != n:
                D[n][nn] = dist + 1
                q.append((nn, D[n][nn]))


for n in range(1, N + 1):
    bfs(n)

a = N + 1
b = N + 1
l = 1 << 31

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            continue
        temp = 0
        for n in range(1, N + 1):
            temp += min(D[i][n], D[j][n])
        temp *= 2
        temp_i = min(i,j)
        temp_j = max(i,j)
        if temp < l:
            a = temp_i
            b = temp_j
            l = temp
        elif temp == l:
            if a > temp_i:
                a = temp_i
                b = temp_j
            if a == temp_i and b > temp_j:
                b = temp_j

print(a, b, l)
