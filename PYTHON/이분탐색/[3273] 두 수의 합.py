import sys
input = sys.stdin.readline
#
# N = int(input())
# nums = sorted(list(map(int, input().split())))
# X = int(input())
# print(nums)
#
# def bin_search(a, l, r, x):
#     print(l, r, x)
#     while l <= r:
#         mid = (l + r) // 2
#         if a[mid] == x:
#             return True
#         if a[mid] < x:
#             l = mid + 1
#         else:
#             r = mid - 1
#     return False
#
#
# nums.sort()
# ans = 0
# for i in range(N - 1):
#     if bin_search(nums, i + 1, N - 1, X - nums[i]):
#         ans += 1
#
# print(ans)

N = int(input())
nums = sorted(list(map(int, input().split())))
X = int(input())
L, R = 0, N - 1
cnt = 0
while L < R:
    s = nums[L] + nums[R]
    if s == X:
        cnt += 1
        L += 1
        continue
    if s > X:
        R -= 1
        continue
    if s < X:
        L += 1
        continue
print(cnt)