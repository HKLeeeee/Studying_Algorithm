import sys
input = sys.stdin.readline
N = int(input())
like_list = [[] for _ in range(N ** 2 + 1)]
seated = [[0 for _ in range(N)] for _ in range(N)]
order = []
for _ in range(N ** 2):
    a, b, c, d, e = map(int, input().split())
    like_list[a] = [b, c, d, e]
    order.append(a)


def find_seat(s):
    candidate = []  # (x, y, 인접한 칸에 좋아하는 학생 수, 인접한 칸에 비어있는 자리 수)
    for i in range(N):
        for j in range(N):
            if seated[i][j] != 0:
                continue

            like = 0
            empty = 0
            for (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if seated[ni][nj] == 0:
                        empty += 1
                    elif seated[ni][nj] in like_list[s]:
                        like += 1

            candidate.append((i, j, like, empty))

    candidate.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    return candidate[0][0], candidate[0][1]


def calc_happiness():
    total = 0
    for i in range(N):
        for j in range(N):
            like = 0
            s = seated[i][j]
            for (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N and seated[ni][nj] in like_list[s]:
                    like += 1
            if like > 0:
                total += 10 ** (like-1)
    return total

for student in order:
    x, y = find_seat(student)
    seated[x][y] = student

print(calc_happiness())