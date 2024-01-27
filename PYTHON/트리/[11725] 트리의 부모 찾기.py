import sys
from collections import deque
input = sys.stdin.readline
# sys.setrecursionlimit(100005)

N = int(input())
adj_list = [[] for _ in range(N + 1)]
ans = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    i, j = map(int, input().split())
    adj_list[i].append(j)
    adj_list[j].append(i)


def bfs():
    q = deque()
    for t in adj_list[1]:
        q.append(t)
        ans[t] = 1

    while q:
        n = q.popleft()
        for t in adj_list[n]:
            if ans[t] == 0:
                q.append(t)
                ans[t] = n


def dfs(parent):
    for node in adj_list[parent]:
        if ans[node] == 0:
            ans[node] = parent
            dfs(node)

bfs()
# dfs(1)
for i in range(2, N + 1):
    print(ans[i])
