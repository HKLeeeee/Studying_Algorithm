import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
knight_x, knight_y = map(int, input().split())
board = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]

other = []
for _ in range(M):
    other.append(tuple(map(int, input().split())))

q = deque()
q.append((knight_x, knight_y, 0))
board[knight_x][knight_y] = 0
while q:
    x, y, t = q.popleft()

    for dx, dy in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
        nx = x + dx
        ny = y + dy

        if 0 < nx <= N and 0 < ny <= N and board[nx][ny] < 0:
            board[nx][ny] = t + 1
            q.append((nx, ny, t + 1))

for ox, oy in other:
    print(board[ox][oy], end=' ')