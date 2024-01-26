import sys
input = sys.stdin.readline
N = int(input())
stairs = [int(input()) for _ in range(N)]
def solve() :
    dp = [[0 for _ in range(N)] for _ in range(2)]
    dp[0][0] = stairs[0]
    if N == 1:
        return stairs[0]
    dp[0][1] = stairs[1]
    dp[1][1] = stairs[0] + stairs[1]

    for i in range(2, N):
        dp[0][i] = max(dp[0][i-2], dp[1][i-2]) + stairs[i]
        dp[1][i] = dp[0][i-1] + stairs[i]

    return max(dp[0][N-1], dp[1][N-1])
print(solve())