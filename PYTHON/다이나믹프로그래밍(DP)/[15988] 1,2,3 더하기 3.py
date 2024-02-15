import sys
input = sys.stdin.readline

T = int(input())
dp = [0, 1, 2, 4]

def solve(n):
    l = len(dp)
    for i in range(l, n+1):
        dp.append(sum(dp[i-3:i])%1000000009)
    print(dp[N])

for _ in range(T):
    N = int(input())
    if N <= len(dp) - 1:
        print(dp[N])
        continue
    else:
        solve(N)
