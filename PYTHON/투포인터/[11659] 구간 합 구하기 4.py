import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
acc_sum = [0 for _ in range(N+1)]
temp = 0
for i, n in enumerate(nums) :
    temp += n
    acc_sum[i+1] = temp

for _ in range(M):
    i, j = map(int, input().split())
    print(acc_sum[j] - acc_sum[i-1])
