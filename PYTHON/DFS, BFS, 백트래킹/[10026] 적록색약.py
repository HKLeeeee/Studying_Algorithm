import sys
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline
N = int(input())
graph = [input().strip() for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
a, b = 0, 0

def dfs(x, y, color):
    visit[x][y] = True
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
            if color == graph[nx][ny]:
                dfs(nx, ny, color)

visit = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            color = graph[i][j]
            dfs(i, j, color)
            a += 1

visit = [[False for _ in range(N)] for _ in range(N)]
for i, line in enumerate(graph):
    graph[i] = line.replace("R", "G")

for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            color = graph[i][j]
            dfs(i, j, color)
            b += 1
print(a, b)
