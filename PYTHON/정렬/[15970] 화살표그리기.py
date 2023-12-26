import sys

input = sys.stdin.readline

N = int(input())
dots = [tuple(map(int, input().split())) for _ in range(N)]  # [(pos, color)]
dots.sort(key=lambda x: (x[1], x[0]))

dist = abs(dots[0][0] - dots[1][0]) + abs(dots[N-1][0] - dots[N-2][0])

for i in range(1, N-1):
    curr_dist = 100000
    if dots[i - 1][1] == dots[i][1]:
        curr_dist = min(curr_dist, abs(dots[i - 1][0] - dots[i][0]))
    if dots[i][1] == dots[i + 1][1]:
        curr_dist = min(curr_dist, abs(dots[i][0] - dots[i + 1][0]))
    dist += curr_dist

print(dist)
