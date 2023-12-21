import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [input() for _ in range(N)]
visit = [[[0, 0] for _ in range(M)] for _ in range(N)]
visit[0][0][0] = 1


def bfs():
    queue = deque([[0, 0, 0]])  # x, y, crush

    while queue:
        x, y, flag = queue.popleft()
        if x == N - 1 and y == M - 1:
            return visit[x][y][flag]

        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + i
            ny = y + j
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == '0' and visit[nx][ny][flag] == 0:
                    visit[nx][ny][flag] = visit[x][y][flag] + 1
                    queue.append([nx, ny, flag])
                elif board[nx][ny] == '1' and flag == 0:
                    visit[nx][ny][1] = visit[x][y][0] + 1
                    queue.append([nx, ny, 1])
    return -1


print(bfs())

# https://angelatto.tistory.com/53