import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

def bfs(i):
    q = deque()
    q.append(i)
    num = [ -1 for _ in range(N+1)]
    num[i] = 0
    while q:
        node = q.popleft()
        for friend in adj_list[node]:
            if num[friend] < 0:
                num[friend] = num[node] + 1
                q.append(friend)
    return sum(num)

minV, minIdx = bfs(1), 1
for i in range(2, N + 1):
    v = bfs(i)
    if minV > v:
        minV, minIdx = v, i

print(minIdx)


# min_kebin = 1 << 31
# num = 0
# for i in range(1, N + 1):
#     kebin_number = bfs(i)
#     if min_kebin > kebin_number:
#         num = i
#         min_kebin = kebin_number
# print(num)