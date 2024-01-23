import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

max_water = list(map(int, input().split()))
queue = deque()
queue.append([0, 0, max_water[2]])
ans = []
mov = [[0, 1], [1, 0], [1, 2], [2, 1], [0, 2], [2, 0]]
check = [[0, 0, max_water[2]]]

while queue:
    s = queue.popleft()

    if s[0] == 0:
        ans.append(s[2])

    for m in mov:
        state = deepcopy(s)

        f, t = m
        if state[f] == 0:
            continue
        if state[t] >= max_water[t]:
            continue
        amount = max_water[t] - state[t]
        if state[f] > amount:
            state[f] -= amount
            state[t] += amount
        else:
            state[t] += state[f]
            state[f] = 0

        if state not in check:
            check.append(state)
            queue.append(state)
ans.sort()
print(*ans)
