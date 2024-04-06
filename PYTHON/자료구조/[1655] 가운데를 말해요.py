import sys
import heapq
input = sys.stdin.readline
N = int(input())
leftHeap = []
rightHeap = []
for i in range(N):
    num = int(input())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else :
        heapq.heappush(rightHeap, num)

    if len(rightHeap) > 0 and -leftHeap[0] > rightHeap[0]:
        left = heapq.heappop(leftHeap)
        right = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -right)
        heapq.heappush(rightHeap, -left)

    print(-leftHeap[0])
