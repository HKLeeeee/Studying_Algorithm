# from collections import Counter
# import sys
# input = sys.stdin.readline
# N = int(input())
# numbers = [int(input()) for _ in range(N)]
# counter = Counter(numbers)
# most_common = sorted(counter.most_common(), key=lambda x: (-1*x[1], x[0]))
# print(most_common[0][0])

import sys

input = sys.stdin.readline
N = int(input())
numbers = sorted([int(input()) for _ in range(N)])

curr_cnt = 1
max_cnt = 1
mode = numbers[0]
for i in range(1, N):
    if numbers[i - 1] != numbers[i]:
        curr_cnt = 1
    else:
        curr_cnt += 1

    if curr_cnt > max_cnt:
        mode = numbers[i]
        max_cnt = curr_cnt

print(mode)
