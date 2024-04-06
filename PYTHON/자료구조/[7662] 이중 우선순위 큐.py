import heapq
def solution(operations):
    min_heap = []
    max_heap = []
    activated = {}
    cnt = 0
    for i, op in enumerate(operations):
        command, action = op.split()
        action = int(action)
        if command == "I":
            heapq.heappush(min_heap, (action, i))
            heapq.heappush(max_heap, (-action, i))
            activated[i] = True
            cnt += 1
        else:
            if cnt <= 0 :
                continue
            if action == 1:
                while max_heap and not activated[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    (n, i) = heapq.heappop(max_heap)
                    activated[i] = False
            else:
                while min_heap and not activated[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    (n, i) = heapq.heappop(min_heap)
                    activated[i] = False
            cnt -= 1

    if cnt == 0:
        return print("EMPTY")
    while max_heap and not activated[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not activated[min_heap[0][1]]:
        heapq.heappop(min_heap)
    return print(-max_heap[0][0], min_heap[0][0])

import sys
input = sys.stdin.readline
if __name__ == "__main__" :
    T = int(input())
    for _ in range(T):
        k = int(input())
        operations = [input().rstrip() for _ in range(k)]
        solution(operations)
