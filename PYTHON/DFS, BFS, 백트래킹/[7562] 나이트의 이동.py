import sys
from collections import deque

input = sys.stdin.readline
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]


def move_knight(N, start, end):
    visit = [[0] * N for _ in range(N)]
    d_x, d_y = end
    q = deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        if x == d_x and y == d_y:
            return visit[x][y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visit[nx][ny] == 0:
                q.append((nx, ny))
                visit[nx][ny] = visit[x][y] + 1


answer = []
T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    start = tuple(map(int, input().strip().split()))
    end = tuple(map(int, input().strip().split()))
    answer.append(move_knight(N, start, end))

for a in answer:
    print(a)
