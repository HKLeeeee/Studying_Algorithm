import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
x, y = -1, -1
for i, line in enumerate(board):
    for j, b in enumerate(line):
        if b == 9:
            y = j
            x = i

def possible_meal(ox, oy, size):
    # 현재 위치에서 먹을 수 있는 물고기 수 == 이동 가능한 위치에 있는 현재 상어의 크기보다 작은 물고기
    candidate = []
    visit = [[False for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((ox, oy, 0))

    while q:
        x, y, t = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and board[nx][ny] <= size:
                visit[nx][ny] = True
                if 0 < board[nx][ny] < size:
                    candidate.append((nx, ny, t+1))
                q.append((nx, ny, t+1))

    # 가장 가까운 -> 가장 위 -> 가장 왼쪽 x, y 좌표로 정렬
    return sorted(candidate, key=lambda info: (info[2], info[0], info[1]))


def baby_shark(x, y):
    # init, 처음 상어의 크기는 2
    size = 2
    left = size
    time = 0

    while True:
        board[x][y] = 0
        # 현재 위치에서 먹을 수 있는 물고기 후보 탐색
        candidate = possible_meal(x, y, size)
        # 없으면 time 리턴
        if len(candidate) == 0:
            return time

        # 있으면 가장 가까운 곳으로 이동해서 냠
        left -= 1
        nx, ny, dist = candidate[0]
        time += dist
        if left == 0:
            size += 1
            left = size
        x, y = nx, ny


print(baby_shark(x, y))
