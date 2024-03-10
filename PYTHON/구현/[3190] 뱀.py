import sys
from collections import deque
input = sys.stdin.readline

def change_direction(now, d):
    if now == (0, 1):
        return (1, 0) if d == "D" else (-1, 0)
    elif now == (0, -1):
        return (-1, 0) if d == "D" else (1, 0)
    elif now == (1, 0):
        return (0, -1) if d == "D" else (0, 1)
    elif now == (-1, 0):
        return (0, 1) if d == "D" else (0, -1)


N = int(input())
K = int(input())
apples = [tuple(map(int, input().split())) for _ in range(K)]
board = [["" for _ in range(N + 1)] for _ in range(N + 1)]
for (ax, ay) in apples:
    board[ax][ay] = "A"
board[1][1] = "S"

L = int(input())
move = list(map(lambda x: [int(x[0]), x[1]], [input().split() for _ in range(L)]))

snake = deque()
snake.append((1, 1))
direction = (0, 1)
time = 1

while True:
    x, y = snake[-1]

    nx, ny = x + direction[0], y + direction[1]
    if nx < 1 or nx > N or ny < 1 or ny > N :
        break
    if board[nx][ny] == "S":
        break

    if board[nx][ny] == "A":
        board[nx][ny] = "S"
    elif board[nx][ny] == "":
        board[nx][ny] = "S"
        last_x, last_y = snake.popleft()
        board[last_x][last_y] = ""
    snake.append((nx, ny))

    if len(move) > 0 and move[0][0] == time:
        direction = change_direction(direction, move[0][1])
        move = move[1:]
    time += 1

print(time)


