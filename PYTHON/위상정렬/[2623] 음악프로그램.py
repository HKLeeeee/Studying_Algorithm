import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
in_degree = [0 for _ in range(N + 1)]
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    order = list(map(int, input().split()))[1:]
    for i in range(len(order) - 1):
        x, y = order[i], order[i + 1]
        adj_list[x].append(y)
        in_degree[y] += 1

q = deque()
for i in range(1, N + 1):
    if in_degree[i] == 0:
        q.append(i)

ans = []
while q:
    singer = q.popleft()
    ans.append(singer)
    for next in adj_list[singer]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            q.append(next)
if len(ans) == N :
    for s in ans:
        print(s)
else :
    print(0)
