import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visit = [False for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    for g in graph[node]:
        if not visit[g]:
            visit[g] = True
            dfs(g)
    return 1

cnt = 0
for s in range(1, N+1):
    if not visit[s]:
        cnt += dfs(s)

print(cnt)