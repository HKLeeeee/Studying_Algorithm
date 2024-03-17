import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)] # [무게, 가격]
bags = [int(input()) for _ in range(K)]

jewels.sort()
bags.sort()
ans, idx = 0, 0
candi = []
for bag in bags:
    while idx < N and jewels[idx][0] <= bag:
        heapq.heappush(candi, -jewels[idx][1])
        idx += 1

    if candi:
        ans -= heapq.heappop(candi)

print(ans)

# 보석을 무게 순으로 정렬 # 가벼운 것 부터
# 가방을 무게 순으로 정렬