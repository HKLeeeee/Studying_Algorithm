import sys
input = sys.stdin.readline
A, B = input().strip().split()

def str2deci_arr(S):
    num = []
    for s in S:
        if ord(s) >= 97:
            num.append(ord(s) - 86)
        else:
            num.append(int(s) + 1)
    return num


def solution(A, B):
    ans = ''
    a_min_base = max(max(str2deci_arr(A)), 2)
    b_min_base = max(max(str2deci_arr(B)), 2)
    for i in range(a_min_base, 37):
        a = int(A, i)
        if a >= 2 ** 63:
            continue

        for j in range(b_min_base, 37):
            if i == j:
                continue
            b = int(B, j)
            if b >= 2 ** 63:
                continue

            if a == b:
                if len(ans) > 0:
                    return "Multiple"
                else:
                    ans = f"{a} {i} {j}"

    return ans if len(ans) > 0 else "Impossible"

print(solution(A, B))
## 진번 변환
def to_decimal(notation, string):
    num = []
    for s in string:
        if ord(s) >= 97:
            num.append(ord(s) - 87)
        else:
            num.append(int(s))

    deci = 0
    for n in num:
        deci = deci * notation + n
    return deci
