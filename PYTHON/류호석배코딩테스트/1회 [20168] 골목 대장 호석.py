# import sys
# from collections import deque
#
# input = sys.stdin.readline
# N, M, A, B, C = map(int, input().split())
# adj_list = [[] for _ in range(N + 1)]
# for _ in range(M):
#     a, b, m = map(int, input().split())
#     adj_list[a].append((b, m))
#     adj_list[b].append((a, m))
# ans = 1001
# q = deque()  # deque((node, 지금까지 최대 수금액, 여기까지 오는데 총 드는 금액, 여기까지 오는데 지나온 길))
# q.append([A, 0, 0, []])
# while q:
#     node, max_fee, acc_fee, visited = q.popleft()
#     if node == B:
#         if acc_fee <= C:
#             ans = min(ans, max_fee)
#         continue
#
#     for (nn, fee) in adj_list[node]:
#         if nn not in visited and acc_fee + fee <= C:
#             q.append([nn, max(max_fee, fee), acc_fee + fee, visited + [nn]])
#
# if ans == 1001:
#     ans = -1
# print(ans)

import sys
import heapq

input = sys.stdin.readline
N, M, A, B, C = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, m = map(int, input().split())
    adj_list[a].append((b, m))
    adj_list[b].append((a, m))
ans = 21
dist = [1 << 31 for _ in range(N + 1)]
dist[A] = 0
q = [[0, 0, 0, A]]  # (dist, 지금까지 최대 수금액, 여기까지 오는데 총 드는 금액, node))

while q:
    d, max_fee, acc_fee, node = heapq.heappop(q)
    if d > dist[node]:
        continue

    if node == B:
        if acc_fee <= C:
            ans = min(ans, max_fee)
            break
    else:
        for (nn, fee) in adj_list[node]:
            if acc_fee + fee <= C and dist[nn] > d+1:
                dist[nn] = d+1
                heapq.heappush(q, [dist[nn], max(max_fee, fee), acc_fee + fee, nn])
if ans == 21:
    ans = -1
print(ans)
