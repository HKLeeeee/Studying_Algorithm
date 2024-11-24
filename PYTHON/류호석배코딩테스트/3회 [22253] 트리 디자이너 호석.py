import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
adj_list = [ [] for _ in range(N+1)]
node_nums = list(map(int, input().split()))
edges_nums = [0 for _ in range(N+1)]
level = [-1 for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    edges_nums[x] += 1
    edges_nums[y] += 1
    adj_list[x].append(y)
    adj_list[y].append(x)

def is_asc(nodes):
    prev = nodes[0]
    for n in nodes[1:]:
        if prev > n :
            return False
        prev = n
    return True

def dfs():
    stack = [1]

    while stack:
        top = stack.pop()


