import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]
acc_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    temp = 0
    for j in range(N):
        temp += nums[i][j]
        acc_sum[i+1][j+1] = temp

for _ in range(M):
    start_x, start_y, end_x, end_y = map(int, input().split())
    ans = 0
    for x in range(start_x, end_x + 1):
        ans += acc_sum[x][end_y] - acc_sum[x][start_y - 1]
    print(ans)