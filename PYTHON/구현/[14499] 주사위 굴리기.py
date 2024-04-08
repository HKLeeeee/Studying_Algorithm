import sys

input = sys.stdin.readline

N, M, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
dice = [0,0,0,0,0,0]
up = 1


def turn(dir):
    global dice
    a, b, c, d, e, f = dice
    if dir == 1:
        dice = [a, e, c, f, d, b]
    elif dir == 2:
        dice = [a, f, c, e, b, d]
    elif dir == 3:
        dice = [b, c, d, a, e, f]
    elif dir == 4:
        dice = [d, a, b, c, e, f]


d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
for o in order:
    nx, ny = x + d[o - 1][0], y + d[o - 1][1]
    if 0 > nx or nx >= N or 0 > ny or ny >= M:
        continue
    x, y = nx, ny
    turn(o)

    if board[x][y] == 0:
        board[x][y] = dice[3]
    else:
        dice[3] = board[x][y]
        board[x][y] = 0

    print(dice[1])

