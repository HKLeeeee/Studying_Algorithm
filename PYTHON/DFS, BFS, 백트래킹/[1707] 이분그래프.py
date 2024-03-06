import sys

input = sys.stdin.readline


def solution(adj_list):
    pass


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    solution(adj_list)
