import sys
input = sys.stdin.readline
N = int(input())

dp = [[1 for _ in range(10)] for _ in range(N+1)]

dp[1] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(2, N + 1):
    for j in range(10):
        dp[i][j] = sum(dp[i - 1][:j+1]) % 10007

print(sum(dp[N-1]) % 10007)
print(dp)