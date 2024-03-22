import sys
input = sys.stdin.readline

N1, M1 = map(int, input().split())
A = [input().strip() for _ in range(N1)]

N2, M2 = map(int, input().split())
B = [input().strip() for _ in range(N2)]

def rotate(origin, n, m):
    temp = [['' for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            temp[j][n - i - 1] = origin[i][j]
    return temp, m, n


def possible(shift_row, shift_col):
    for ai in range(N1):
        for aj in range(M1):
            if A[ai][aj] == "0":
                continue
            bi = ai + shift_row
            bj = aj + shift_col
            if 0 <= bi < N2 and 0 <= bj < M2 and B[bi][bj] == "1":
                return False
    return True


res = 10001
for _ in range(4):  # 회전
    B, N2, M2 = rotate(B, N2, M2)
    # 평행이동
    pos = True
    for i in range(-51, 51):
        for j in range(-51, 51):
            if possible(i, j):
                row = max(N2, i + N1) - min(0, i)
                col = max(M2, j + M1) - min(0, j)
                res = min(res, row * col)

print(res)
