import sys
input = sys.stdin.readline
M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
way = [[-1] * N for _ in range(M)]
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1

    if way[x][y] != -1: # 이미 계산한 곳이라면 계산한 값 리턴
        return way[x][y]

    way[x][y] = 0 # 방문체크
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and board[x][y] > board[nx][ny]:
            way[x][y] += dfs(nx, ny)
    return way[x][y]


print(dfs(0, 0))
