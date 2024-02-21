import heapq, sys
input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
adj_list = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append((v, w))

dist = [1 << 31 for _ in range(V + 1)]
heap = [(0, start)]
while heap:
    time, pos = heapq.heappop(heap)
    if time >= dist[pos]:
        continue

    for (destination, weight) in adj_list[pos]:
        dist[destination] = time + weight
        heapq.heappush(heap, (dist[destination], destination))

for d in dist[1:]:
    if d == 1 << 31:
        print("INF")
    else:
        print(d)
