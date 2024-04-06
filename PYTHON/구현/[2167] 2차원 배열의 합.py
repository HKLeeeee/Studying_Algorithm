import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [list(map(int, input().split())) for _ in range(N)]
T = int(input())

added_nums = [[]]
for i in range(N):
    temp = [0 for _ in range(M+1)]
    for j in range(1, M+1):
        temp[j] += (nums[i][j-1] + temp[j-1])
    added_nums.append(temp)

for _ in range(T):
    i, j, x, y = map(int, input().split())
    s = 0
    for l in range(i, x+1):
        s += added_nums[l][y]
        s -= added_nums[l][j-1]
    print(s)