import sys

N = 10000
M = 10000
# board = [[[0, 0] for _ in range(M)] for _ in range(N)]
# board = [[0] * M for _ in range(N)]
board = [0 for _ in range(1000000000)]  ## 10억 길이의 배열의 크기 8806.512088 MB

print(f"{sys.getsizeof(board) * 1e-6} MB")
