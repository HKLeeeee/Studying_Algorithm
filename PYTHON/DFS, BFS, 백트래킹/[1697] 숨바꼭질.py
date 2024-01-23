import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
visit = [0 for _ in range(100001)]
q = deque()
q.append(N)

while q:
    pos = q.popleft()
    if pos == K:
        break

    for np in [pos - 1, pos + 1, pos * 2]:
        if 0 <= np < 100001 and visit[np] == 0:
            q.append(np)
            visit[np] = visit[pos] + 1

print(visit[K])
