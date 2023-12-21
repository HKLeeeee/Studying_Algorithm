import sys
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []
selected = []
min_dist = 999999999
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])
visited = [False for _ in range(len(chicken))]


def calc_dist(chicken, home):
    return abs(chicken[0]-home[0]) + abs(chicken[1]-home[1])


def solve(cnt, start):
    global min_dist
    if cnt == M:
        chicken_dist = 0
        for h in home:
            each_chicken_dist = 100
            for ch in selected:
                each_chicken_dist = min(each_chicken_dist, calc_dist(ch, h))
            chicken_dist += each_chicken_dist
        min_dist = min(min_dist, chicken_dist)

    else:
        for i in range(start, len(chicken)):
            ch = chicken[i]
            if not visited[i]:
                selected.append(ch)
                visited[i] = True
                solve(cnt+1, i)
                selected.pop()
                visited[i] = False


solve(0, 0)
print(min_dist)
