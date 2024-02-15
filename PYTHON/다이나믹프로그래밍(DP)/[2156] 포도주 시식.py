import sys
input = sys.stdin.readline

N = int(input())
wine = [int(input()) for _ in range(N)]


def solve():
    dp = [[0, 0, 0] for _ in range(N)]
    if N == 1:
        return wine[0]

    dp[0] = [wine[0], -1, -1]
    dp[1] = [wine[1], wine[0] + wine[1], wine[1]]
    for i in range(2, N):
        dp[i][0] = max(dp[i - 2]) + wine[i]
        dp[i][1] = dp[i - 1][0] + wine[i]
        dp[i][2] = max(dp[i-1])
    return max(dp[N - 1])

print(solve())