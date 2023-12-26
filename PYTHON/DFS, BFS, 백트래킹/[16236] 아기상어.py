import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
baby_shark_size = 2
size_up_left = 2
cnt = 0
fish_left = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            pos = [i, j]
            break
        if board[i][j] != 0:
            fish_left.append([i, j])

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
queue = deque()
queue.append(pos)


def dist(shark, fish):
    return abs(shark[0] - fish[0]) + abs(shark[1] - fish[1])


while len(fish_left) > 0:
    dist_list = [dist(pos, f) for f in fish_left]
    for idx, [x, y] in enumerate(fish_left):
        if board[x][y] > baby_shark_size :
            dist_list[idx] = 9999
    if len(dist_list) == 0:
        break

    min_dist = min(dist_list)
    cand = []
    for idx in range(len(dist_list)):
        if dist_list[idx] == min_dist:
            cand.append(fish_left[idx])

    cand = sorted(cand, key=lambda x: (x[0], x[1]))
    print(cand)
    x, y = cand[0]
    cnt += board[x][y]
    fish_left.remove(cand[0])
    pos = [x, y]
    if size_up_left == 1:
        baby_shark_size += 1
        size_up_left = baby_shark_size
    else:
        size_up_left -= 1

print(cnt)
