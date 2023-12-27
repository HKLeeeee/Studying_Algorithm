import sys
input = sys.stdin.readline

def solve(A, B):
    cnt = 0
    for a in A:
        L = 0
        R = len(B) - 1
        result = -1
        while L <= R:
            mid = int((L + R) / 2)
            if B[mid] >= a:
                R = mid - 1
            elif B[mid] < a:
                result = mid
                L = mid + 1
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
