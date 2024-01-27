import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    indegree[j] += 1
    adj_list[i].append(j)

q = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
ans = []
while q :
    t = q.popleft()
    ans.append(t)
    for node in adj_list[t] :
        indegree[node] -= 1
        if indegree[node] == 0 :
            q.append(node)
print(*ans)