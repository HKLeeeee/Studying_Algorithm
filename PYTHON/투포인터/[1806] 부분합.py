import sys

input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))
R = 0
curr_sum = 0
min_len = N + 1

for L in range(N):
    while curr_sum < S and R < N:
        curr_sum += nums[R]
        R += 1

    if curr_sum >= S:
        min_len = min(min_len, R - L)

    curr_sum -= nums[L]

print(min_len if min_len < N + 1 else 0)
# 투포인터 O(N)

# start, end = 0, 0
# min_len = N + 1
# curr_sum = 0
#
# while start < N and end < N:
#     curr_sum += nums[end]
#     end += 1
#     if curr_sum >= S:
#         min_len = min(min_len, end - start)
#         start += 1
#         end = start + 1
#         curr_sum = nums[start]
#
# print(min_len if min_len < N + 1 else 0)
# => O(N^2) 풀이