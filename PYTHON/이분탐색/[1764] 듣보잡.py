import sys

input = sys.stdin.readline

N, M = map(int, input().split())

not_see = [input().strip() for _ in range(N)]
not_listen = [input().strip() for _ in range(M)]

not_see_listen = sorted(list(set(not_see).intersection(set(not_listen))))

print(len(not_see_listen))
for p in not_see_listen:
    print(p)