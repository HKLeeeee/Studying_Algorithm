import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().strip().split())
lines = [input().strip() for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visit = [[0] * M for _ in range(N)]
q = deque()
q.append((0, 0))
visit[0][0] = 1
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] == 0 and lines[nx][ny] == '1':
            q.append((nx, ny))
            visit[nx][ny] = visit[x][y] + 1

print(visit[N-1][M-1])

