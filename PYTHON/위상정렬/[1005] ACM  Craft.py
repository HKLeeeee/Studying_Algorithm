import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    building = list(map(int, input().split()))
    adj_list = [[] for _ in range(N + 1)]
    indegree = [0 for _ in range(N + 1)]
    indegree_time = [[0] for _ in range(N+1)]
    for _ in range(K):
        i, j = map(int, input().split())
        adj_list[i].append(j)
        indegree[j] += 1
    target = int(input())

    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append((-1, i))
            indegree_time[i].append(building[i-1])

    while q:
        f, t = q.popleft()
        for node in adj_list[t]:
            indegree_time[node].append(max(indegree_time[t]) + building[node - 1])
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append((t, node))
    print(max(indegree_time[target]))
