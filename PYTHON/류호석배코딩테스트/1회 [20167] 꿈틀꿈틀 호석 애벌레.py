# import sys
# input = sys.stdin.readline
#
# N, K = map(int, input().split())
# branch = list(map(int, input().split()))
# ans = -1

def rec_func(cnt, eat_amount, energy, eat_last):
    global ans
    if cnt == N:
        ans = max(ans, energy)
    else:
        if eat_amount + branch[cnt] >= K:
            energy += (eat_amount + branch[cnt]) - K
            rec_func(cnt + 1, 0, energy, False)
        else:
            rec_func(cnt + 1, eat_amount + branch[cnt], energy, True)

        if not eat_last:
            rec_func(cnt + 1, eat_amount, energy, False)


# rec_func(0, 0, 0, False)
# print(ans)

#####################
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
branch = list(map(int, input().split()))
ans = -1
L, R = 0, -1
curr_sum = 0
intervals = [[] for _ in range(N)]
while L < N:
    while curr_sum < K and R + 1 < N:
        R += 1
        curr_sum += branch[R]
        if curr_sum >= K :
            intervals[R].append([L, curr_sum - K])

    curr_sum -= branch[L]
    L += 1

Dy = [0 for _ in range(N)]
if len(intervals[0]) > 0:
    Dy[0] = intervals[0][0][1]

for i in range(1, N):
    Dy[i] = Dy[i-1]
    for (left, satisfy) in intervals[i]:
        Dy[i] = max(Dy[i], Dy[left - 1] + satisfy)

print(Dy[-1])

