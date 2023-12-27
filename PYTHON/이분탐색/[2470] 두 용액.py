import sys

input = sys.stdin.readline


def lower_bound(a, L, R, x):  # 배열, Left, Right, 탐색할 목표
    res = R + 1
    while L <= R:
        mid = (L + R) // 2
        if a[mid] >= x:
            res = mid
            R = mid - 1
        else:
            L = mid + 1
    return res  # 탐색 결과의 인덱스


if __name__ == "__main__":
    N = int(input())  # 2 이상 100,000 이하
    nums = sorted(list(map(int, input().split())))

    best_sum = 1 << 31
    v1, v2 = 0, 0

    for i in range(N - 1):
        candidate = lower_bound(nums, i + 1, N - 1, -nums[i])
        if i < candidate - 1 and abs(nums[i] + nums[candidate - 1]) < best_sum:
            best_sum = abs(nums[i] + nums[candidate - 1])
            v1, v2 = nums[i], nums[candidate - 1]
        if candidate < N and best_sum > abs(nums[i] + nums[candidate]):
            best_sum = abs(nums[i] + nums[candidate])
            v1, v2 = nums[i], nums[candidate]

    print(v1, v2)
