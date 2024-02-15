import heapq
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    f, t, p = map(int, input().split())
    adj_list[f].append((p, t))

start, end = map(int, input().split())
dist = [10_000_000_001 for _ in range(N + 1)]
dist[start] = 0
heap = []

for v in adj_list[start]:
    heapq.heappush(heap, v)
while heap:
    p, t = heapq.heappop(heap)
    if p >= dist[t]:
        continue
    dist[t] = p
    for (vp, vt) in adj_list[t]:
        heapq.heappush(heap, (vp + p, vt))

print(dist[end])
