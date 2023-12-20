import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

def virus():
    new_board = deepcopy(board)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque(virus_loc)
    while q :
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and new_board[nx][ny] == 0:
                q.append([nx, ny])
                new_board[nx][ny] = 2
    return new_board

def count_zero(new_board) :
    cnt = 0
    for line in new_board:
        for l in line:
           if l == 0 :
            cnt += 1
    return cnt


def solve(cnt):
    global max_
    if cnt == 3:
        result = virus()
        max_ = max(max_, count_zero(result))
    else:
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    board[i][j] = 1
                    solve(cnt + 1)
                    board[i][j] = 0


if __name__ == "__main__":
    import time
    start = time.time()

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_ = 0

    virus_loc = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2:
                virus_loc.append([i, j])
    solve(0)
    print(max_)

    end = time.time()
    print((end - start) * 1000)
