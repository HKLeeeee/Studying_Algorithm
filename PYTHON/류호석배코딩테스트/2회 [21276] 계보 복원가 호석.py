import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
people = input().split()
in_degree = {}
descendant = {}
res = {}

for p in people:
    in_degree[p] = 0
    descendant[p] = []
    res[p] = []

M = int(input())
for _ in range(M):
    x, y = input().split() # 후손, 조상 : 조상 -> 후손 -> 후손
    in_degree[x] += 1
    descendant[y].append(x)

ans = []
q = deque()

for (k, v) in in_degree.items():
    if v == 0:
        ans.append(k)
        q.append((None, k))

ans.sort()
print(len(ans))
print(" ".join(ans))
while q:
    anc, me = q.popleft()
    if anc is not None:
        res[anc].append(me)

    for des in descendant[me]:
        in_degree[des] -= 1
        if in_degree[des] == 0: ## q에 넣는 횟수 줄이기, 직계 후손만 큐에 넣음
            q.append((me, des))

people.sort()
for p in people:
    res[p].sort()
    print(p, len(res[p]), ' '.join(res[p]))