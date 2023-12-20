import sys
from copy import deepcopy

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
max_ = 0
move_direction = [-1 for _ in range(5)]


def up(b):
    board = deepcopy(b)
    n = len(board)
    for j in range(0, n):
        pointer = 0
        for i in range(1, n):
            if pointer == i:
                continue
            if board[pointer][j] == 0 and board[i][j] != 0:
                board[pointer][j] = board[i][j]
                board[i][j] = 0
                continue
            if board[i][j] == 0:
                continue
            if board[pointer][j] == board[i][j]:
                board[pointer][j] *= 2
                pointer += 1
                board[i][j] = 0
                continue
            if board[pointer][j] != board[i][j]:
                for p in range(pointer, i+1):
                    if board[p][j] == 0:
                        board[p][j] = board[i][j]
                        board[i][j] = 0
                        break
                pointer = p
    return board


def down(b):
    board = deepcopy(b)
    n = len(board)
    for j in range(0, n):
        pointer = n - 1
        for i in range(n-2, -1, -1):
            if pointer == i:
                continue
            if board[pointer][j] == 0 and board[i][j] != 0:
                board[pointer][j] = board[i][j]
                board[i][j] = 0
                continue
            if board[i][j] == 0:
                continue
            if board[pointer][j] == board[i][j]:
                board[pointer][j] *= 2
                board[i][j] = 0
                pointer -= 1
                continue
            if board[pointer][j] != board[i][j]:
                for p in range(pointer, i-1, -1):
                    if board[p][j] == 0:
                        board[p][j] = board[i][j]
                        board[i][j] = 0
                        break
                pointer = p
                continue

    return board


def left(b):
    board = deepcopy(b)
    n = len(board)
    for idx in range(n):
        line = board[idx]
        pointer = 0
        for i in range(1, n):
            if pointer == i:
                continue
            if line[pointer] == 0 and line[i] != 0:
                line[pointer] = line[i]
                line[i] = 0
                continue
            if line[i] == 0:
                continue
            if line[pointer] == line[i]:
                line[pointer] *= 2
                line[i] = 0
                pointer += 1
                continue
            if line[pointer] != line[i]:
                for p in range(pointer, i+1):
                    if line[p] == 0:
                        line[p] = line[i]
                        line[i] = 0
                        break
                pointer = p
                continue

    return board


def right(b):
    board = deepcopy(b)
    n = len(board)
    for idx in range(n):
        line = board[idx]
        pointer = n-1
        for i in range(n-2, -1, -1):
            if line[pointer] == 0 and line[i] != 0:
                line[pointer] = line[i]
                line[i] = 0
                continue
            if line[i] == 0:
                continue
            if line[pointer] == line[i]:
                line[pointer] *= 2
                line[i] = 0
                pointer -= 1
                continue
            if line[pointer] != line[i]:
                for p in range(pointer, i-1, -1):
                    if line[p] == 0:
                        line[p] = line[i]
                        line[i] = 0
                        break
                pointer = p
                continue

    return board


def solve(cnt, b):
    global max_
    if cnt == 5:
        for line in b:
            max_ = max(max_, max(line))
    else:
        new_board = up(b)
        solve(cnt + 1, new_board)
        new_board = down(b)
        solve(cnt + 1, new_board)
        new_board = left(b)
        solve(cnt + 1, new_board)
        new_board = right(b)
        solve(cnt + 1, new_board)


solve(0, board)
print(max_)
