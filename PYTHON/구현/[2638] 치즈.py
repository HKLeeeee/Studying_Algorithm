import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def check_inside():
    visit = [[False] * M for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visit[0][0] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                if board[nx][ny] != 1:
                    board[nx][ny] = -1
                    q.append((nx, ny))
                    visit[nx][ny] = True


def check(x, y):
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == -1:
                cnt += 1
            if cnt >= 2:
                return True
    return False


time = 0
while True:
    isEmpty = True
    check_inside()

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                isEmpty = False
                if check(i, j):
                    board[i][j] = 0
    if isEmpty:
        break

    time += 1

print(time)
