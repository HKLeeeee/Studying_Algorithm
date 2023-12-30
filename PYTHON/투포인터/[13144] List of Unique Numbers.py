import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
counts = [0 for _ in range(100001)]

L, R = 0, 0
ans = 0


while L < N:
    while R < N and counts[numbers[R]] == 0:
        counts[numbers[R]] = 1
        R += 1
    ans += R - L

    counts[numbers[L]] = 0
    L += 1
print(ans)