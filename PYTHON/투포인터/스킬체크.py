def two_pointer(purse):
    L, R = 0, 0
    max_sum = -100000 * 500000
    curr = 0
    while R < len(purse):
        if L == R:
            curr += purse[R]
            max_sum = max(max_sum, curr)
            R += 1
            continue

        while R + 1 < len(purse) and purse[R] > 0:
            curr += purse[R]
            R += 1
        max_sum = max(max_sum, curr)

        if R == len(purse) - 1 and purse[R] > 0:
            curr += purse[R]
            max_sum = max(max_sum, curr)

        while L < R:
            curr -= purse[L]
            max_sum = max(max_sum, curr)
            L += 1

    return max_sum


def solution(purse):
    R = 0
    N = len(purse)
    max_sum = -100000 * 500000
    curr = 0
    for L in range(N):
        while R < N and purse[R] >= 0:
            curr += purse[R]
            R += 1
        max_sum = max(max_sum, curr)
        if R < N and purse[R] <= 0 :
            curr += purse[R]
            R += 1
        max_sum = max(max_sum, curr)

        curr -= purse[L]
        max_sum = max(max_sum, curr)

    return max_sum


purse = [2, -1, 4, 3, -2, 100, -3, 6,-3, -3, 9]
print(solution(purse))
