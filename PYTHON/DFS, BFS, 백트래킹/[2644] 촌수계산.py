import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
M = int(input())
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

visit = [False for _ in range(N + 1)]

def bfs(start, target):
    q = deque()
    q.append((start, 0))
    visit[start] = True

    while q:
        p, n = q.popleft()
        if p == target:
            return n

        for adj in adj_list[p]:
            if not visit[adj]:
                q.append((adj, n + 1))
                visit[adj] = True
    return -1

print(bfs(a, b))
