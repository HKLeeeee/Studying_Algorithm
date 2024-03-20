import sys
input = sys.stdin.readline

V, E = map(int, input().split())
adj_list = [[] for _ in range(E+1)]
for _ in range(E):
    A, B = map(int, input().split())
    adj_list[A].append(B)
    adj_list[B].append(A)

