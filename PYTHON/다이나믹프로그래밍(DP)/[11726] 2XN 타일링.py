import sys
input = sys.stdin.readline
N = int(input())

# dp = [0 for _ in range(1001)]
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# for i in range(3, N+1):
#     dp[i] = dp[i-1] + dp[i-2]
# print(dp[N]%10007)

def func(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    return func(n-1) + func(n-2)
print(func(N))