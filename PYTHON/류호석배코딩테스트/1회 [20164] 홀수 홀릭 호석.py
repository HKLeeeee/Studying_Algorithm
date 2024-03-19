import sys

input = sys.stdin.readline

N = input().rstrip()
ans = []
memo = [[] for _ in range(len(N) + 1)]


def solution(N, odd_cnt):
    for n in N:
        if int(n) % 2 == 1:
            odd_cnt += 1
    if len(N) <= 1:
        ans.append(odd_cnt)  # 개선 포인트 : 변수 두 개 (min, max)로 정답 저장
        return

    if len(N) == 2:
        solution(str(int(N[0]) + int(N[1])), odd_cnt)
    elif len(N) >= 3:
        boundary = split_random(len(N))
        for (a, b) in boundary:
            x = N[:a]
            y = N[a:b]
            z = N[b:]
            solution(str(int(x) + int(y) + int(z)), odd_cnt)


def split_random(len_N):
    if len(memo[len_N]) > 0:
        return memo[len_N]
    ans = []
    for i in range(1, len_N - 1):
        for j in range(i + 1, len_N):
            ans.append([i, j])
    return ans


solution(N, 0)
print(min(ans), max(ans))
