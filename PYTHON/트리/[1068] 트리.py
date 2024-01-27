import sys

sys.setrecursionlimit(100005)
input = sys.stdin.readline
N = int(input())
tree = list(map(int, input().split()))
remove_node = int(input())
adj_list = [[] for _ in range(N)]
root = -1
for i, parent in enumerate(tree):
    if parent == -1:
        root = i
    else:
        if i == remove_node:
            continue
        adj_list[parent].append(i)


def dfs(node):
    if len(adj_list[node]) == 0:
        return 1
    ans = 0
    for child in adj_list[node]:
        temp = dfs(child)
        ans += temp
    return ans


if root == remove_node:
    print(0)
else:
    print(dfs(root))


