import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
day = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(visit, r, c):
    q = deque()
    q.append((r, c))
    visit[r][c] = True
    population = A[r][c]
    country = [(r, c)]
    while q:
        x, y = q.popleft()
        curr = A[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and L <= abs(curr - A[nx][ny]) <= R:
                visit[nx][ny] = True
                population += A[nx][ny]
                q.append((nx, ny))
                country.append((nx, ny))

    return population, country


def move() -> bool:
    visit = [[False] * N for _ in range(N)]
    is_moved = False
    for c in range(N):
        for r in range(N):
            if visit[r][c]:
                continue

            population, country = bfs(visit, r, c)
            if population > A[r][c]:
                is_moved = True
                temp = population // len(country)
                for (x, y) in country:
                    A[x][y] = temp

    return is_moved


while move():
    day += 1

print(day)
