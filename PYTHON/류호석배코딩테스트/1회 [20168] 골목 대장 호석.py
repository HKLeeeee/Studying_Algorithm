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

def dijkstra(max_fee): # 조건 내에서 다익스트라
    dist = [1 << 31 for _ in range(N + 1)]
    dist[A] = 0
    heap = [[0, A]]
    while heap:
        acc_fee, node = heapq.heappop(heap)
        if acc_fee > dist[node]: # != ??
            continue

        if node == B and acc_fee <= C:
            return True

        for (nn, fee) in adj_list[node]:
            if fee <= max_fee and dist[nn] > acc_fee + fee:
                dist[nn] = acc_fee + fee
                heapq.heappush(heap, [acc_fee + fee, nn])
    return False

ans = -1
L, R = 0, 10**9
while L <= R: # 파라메트릭 서치
    mid = (L+R) // 2
    if dijkstra(mid):
        ans = mid
        R = mid - 1
    else :
        L = mid + 1

print(ans)
