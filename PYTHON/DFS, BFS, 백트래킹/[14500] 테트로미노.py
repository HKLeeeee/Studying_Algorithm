import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]

maxV = max(map(max, board))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
max_ = 0


def solve(x, y, cnt, value):
    global max_, maxV
    if value + (maxV * (4 - cnt)) <= max_:
        return
    if cnt == 4:
        max_ = max(max_, value)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                if cnt == 2:
                    visit[nx][ny] = True
                    solve(x, y, cnt + 1, value + board[nx][ny])
                    visit[nx][ny] = False

                visit[nx][ny] = True
                solve(nx, ny, cnt + 1, value + board[nx][ny])
                visit[nx][ny] = False


for i in range(N):
    for j in range(M):
        visit[i][j] = True
        solve(i, j, 1, board[i][j])
        visit[i][j] = False
print(max_)
