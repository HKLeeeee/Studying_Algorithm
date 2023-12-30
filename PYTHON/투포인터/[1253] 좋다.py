import sys
input = sys.stdin.readline

N = int(input())
numbers = sorted(list(map(int, input().split())))
ans = 0
for i in range(N):
    target_num = numbers[i]
    L, R = 0, N - 1
    while L < R:
        if L == i:
            L += 1
        elif R == i:
            R -= 1
        else:
            if numbers[L] + numbers[R] > target_num:
                R -= 1
            elif numbers[L] + numbers[R] < target_num:
                L += 1
            else:
                ans += 1
                break
print(ans)
