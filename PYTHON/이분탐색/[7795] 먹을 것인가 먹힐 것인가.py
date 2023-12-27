import sys

input = sys.stdin.readline


def lower_bound(a, L, R, x):
    result = -1
    while L <= R:
        mid = int((L + R) / 2)
        if a[mid] >= x:
            R = mid - 1
        elif a[mid] < x:
            result = mid
            L = mid + 1
    return result


def solve(A, B):
    cnt = 0
    for a in A:
        L, R = 0, len(B) - 1
        result = lower_bound(B, L, R, a)
        cnt += (result + 1)
    return cnt


if __name__ == "__main__":
    T = int(input())
    cases = []
    A_num = []
    B_num = []
    for _ in range(T):
        A, B = map(int, input().split())
        A_num.append(list(map(int, input().split())))
        B_num.append(sorted(list(map(int, input().split()))))

    for i in range(T):
        result = solve(A_num[i], B_num[i])
        print(result)
