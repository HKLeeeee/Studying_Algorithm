import sys
import heapq
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
ans = 0
heapq.heapify(nums)

while len(nums) > 1 :
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    ans += (a+b)
    heapq.heappush(nums, a+b)

print(ans)

