import heapq
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
dist = [100001 for _ in range(100001)]
dist[N] = 0

heap = []
if N * 2 < 100001:
    heap.append((0, N * 2))
if N + 1 < 100001:
    heap.append((1, N + 1))
if N - 1 >= 0:
    heap.append((1, N - 1))
heapq.heapify(heap)

while heap:
    time, pos = heapq.heappop(heap)
    if time >= dist[pos]:
        continue
    dist[pos] = time
    if pos * 2 < 100001:
        heapq.heappush(heap, (time, pos * 2))
    if pos + 1 < 100001:
        heapq.heappush(heap, (time + 1, pos + 1))
    if pos - 1 >= 0:
        heapq.heappush(heap, (time + 1, pos - 1))
print(dist[K])
