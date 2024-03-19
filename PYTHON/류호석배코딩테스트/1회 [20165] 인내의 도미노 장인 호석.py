import sys

input = sys.stdin.readline
N, M, R = map(int, input().split())
board = [[0] * (M + 1)]
for _ in range(N):
    board.append([0] + list(map(int, input().split())))
domino_status = [["S" for _ in range(M + 1)] for _ in range(N + 1)]

direction = {
    "E": [0, 1],
    "W": [0, -1],
    "S": [1, 0],
    "N": [-1, 0]
}
score = 0


def do_attack(x, y, direction):
    global score
    if domino_status[x][y] == "F":  # 예외처리 생각잘하기요
        return

    dx, dy = direction
    cnt = board[x][y]
    while 0 < x <= N and 0 < y <= M and cnt >= 1:
        if domino_status[x][y] == "S":
            score += 1
            domino_status[x][y] = "F"
            cnt = max(cnt - 1, board[x][y] - 1)  # 이걸 생각만 하고 구현을 못했음
        else:
            cnt -= 1
        x += dx
        y += dy


def print_domino():
    for line in domino_status[1:]:
        print(*line[1:])


for _ in range(R):
    x, y, d = input().split()
    do_attack(int(x), int(y), direction[d])

    x, y = map(int, input().split())
    domino_status[x][y] = "S"

print(score)
print_domino()
