import sys
input = sys.stdin.readline

sudoku = list(list(map(int, input().split())) for _ in range(9))
blank = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i, j))


def horizontal_possible(x, y, num):
    if num in sudoku[x]:
        return False
    return True


def vertical_possible(x, y, num):
    for i in range(9):
        if num == sudoku[i][y]:
            return False
    return True


def block_possible(x, y, num):
    for i in range((x//3)*3, (x//3)*3+3):
        for j in range((y//3)*3, (y//3)*3+3):
            if num == sudoku[i][j]:
                return False
    return True


def solve(idx):
    if idx == len(blank):
        for s in sudoku:
            print(*s)
        exit(0)
    else:
        x, y = blank[idx]
        for num in range(1, 10):
            if horizontal_possible(x, y, num) and vertical_possible(x, y, num) and block_possible(x, y, num):
                sudoku[x][y] = num
                solve(idx + 1)
                sudoku[x][y] = 0


solve(0)
