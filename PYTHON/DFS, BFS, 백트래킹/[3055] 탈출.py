import sys
from collections import deque
input = sys.stdin.readline
R, C = map(int, input().split())
forest = [input().strip() for _ in range(R)]
visit = [[-1] * C for _ in range(R)]
water_visit = [[-1] * C for _ in range(R)]
water = deque()
sq = deque()
for i in range(R):
    for j in range(C):
        if forest[i][j] == '*':
            water.append((i, j))
            water_visit[i][j] = 0
            continue
        if forest[i][j] == 'S':
            sq.append((i, j))
            visit[i][j] = 0
            continue
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def water_dfs():
    while water:
        x, y = water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and water_visit[nx][ny] == -1:
                if forest[nx][ny] == '.' or forest[nx][ny] == 'S':
                    water.append((nx, ny))
                    water_visit[nx][ny] = water_visit[x][y] + 1

def bfs():
    while sq:
        x, y = sq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and visit[nx][ny] == -1 :
                if (visit[x][y] + 1 < water_visit[nx][ny]) or (water_visit[nx][ny] == -1):
                    if forest[nx][ny] == 'D':
                        return visit[x][y] + 1
                    if forest[nx][ny] == '.':
                        sq.append((nx, ny))
                        visit[nx][ny] = visit[x][y] + 1
    return 'KAKTUS'

water_dfs()
print(bfs())
