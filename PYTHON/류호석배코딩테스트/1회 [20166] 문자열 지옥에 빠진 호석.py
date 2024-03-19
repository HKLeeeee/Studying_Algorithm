import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [input().rstrip() for _ in range(N)]
target_str = []
ANS_DICT = {}
for _ in range(K):
    s = input().rstrip()
    target_str.append(s)
    ANS_DICT[s] = 0

dx = [1, -1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]


def find(s, x, y, idx) -> int:
    # x, y 출발점에서 시작해서 찾은 문자열
    if len(s) == idx:
        ANS_DICT[s] += 1
        return

    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0:
            nx = N - 1
        elif nx >= N:
            nx = 0
        if ny < 0:
            ny = M - 1
        elif ny >= M:
            ny = 0
        if board[nx][ny] == s[idx]:
            find(s, nx, ny, idx + 1)

for s in target_str:
    if ANS_DICT[s] > 0:
        print(ANS_DICT[s])
        continue

    for i in range(N):
        for j in range(M):
            if board[i][j] == s[0]:
                find(s, i, j, 1)
    print(ANS_DICT[s])
