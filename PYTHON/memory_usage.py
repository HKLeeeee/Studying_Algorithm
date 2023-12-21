import sys

N = 10000
M = 10000
# board = [[[0, 0] for _ in range(M)] for _ in range(N)]
board = [[0] * M for _ in range(N)]

print(f"{sys.getsizeof(board) * 1e-6 } MB")
