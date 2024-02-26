import sys
input = sys.stdin.readline
N = int(input())
solution = list(map(int, input().split()))
solution.sort()
ans = []
best_sum = 3000000001
for L in range(N - 2):
    mid, R = L + 1, N - 1
    while mid < R:
        curr = solution[L] + solution[mid] + solution[R]
        if abs(curr) < abs(best_sum):
            best_sum = curr
            ans = [solution[L], solution[mid], solution[R]]
            if best_sum == 0:
                break
        if curr <= 0 :
            mid += 1
        else:
            R -= 1
print(*ans)