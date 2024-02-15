import sys
input = sys.stdin.readline

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
dp = [[0, 0, 0] for _ in range(N)]
dp[0] = house[0]

for i in range(1, N):
    before = dp[i-1]
    dp[i][0] = min(before[1], before[2]) + house[i][0]
    dp[i][1] = min(before[0], before[2]) + house[i][1]
    dp[i][2] = min(before[0], before[1]) + house[i][2]

print(min(dp[-1]))
