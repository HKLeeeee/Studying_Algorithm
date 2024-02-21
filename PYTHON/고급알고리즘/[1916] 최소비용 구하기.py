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
heapq.heapify(adj_list[start])
heap = adj_list[start]

while heap:
    p, t = heapq.heappop(heap)
    if p >= dist[t]:
        continue
    for (vp, vt) in adj_list[t]:
        dist[vt] = vp + p
        heapq.heappush(heap, (dist[vt], vt))

print(dist[end])
