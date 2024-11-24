import sys

input = sys.stdin.readline

N, M = map(int, input().split())
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북, 동, 남, 서

r, c, curr_d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

result = 0


def clean_possible(x, y):
    if room[x + d[0][0]][y + d[0][1]] == 0:
        return True
    if room[x + d[1][0]][y + d[1][1]] == 0:
        return True
    if room[x + d[2][0]][y + d[2][1]] == 0:
        return True
    if room[x + d[3][0]][y + d[3][1]] == 0:
        return True
    return False


while True:
    if room[r][c] == 0:
        room[r][c] = -1
        result += 1

    if not clean_possible(r, c):
        nr, nc = r - d[curr_d][0], c - d[curr_d][1]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] != 1:
            r, c = nr, nc
            continue
        else:
            print(result)
            break
    else:
        curr_d = (curr_d + 3) % 4
        nr, nc = r + d[curr_d][0], c + d[curr_d][1]
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            r, c = nr, nc
