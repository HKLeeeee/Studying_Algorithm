import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lessons = list(map(int, input().split()))


def determination(S):
    global M
    curr_size, cnt = 0, 1
    for l in lessons:
        if curr_size + l > S:
            cnt += 1
            curr_size = 0
        curr_size += l
    return cnt <= M


L, R = max(lessons), N * 10000
res = R
while L <= R:
    mid = (L + R) // 2
    if determination(mid):
        res = mid
        R = mid - 1
    else:
        L = mid + 1
print(res)

# 결정 문제로 바꾸기
# 크기 S의 블루레이를 M개를 만들면 모든 강의를 녹화할 수 있는가?

# 한 강의 최대 길이 10,000, 최대 강의 수 100,000
# 블루레이 최대 크기 10,000 * 100,000 = 1,000,000,000 (10억) < 24억

# 강의 길이별 정렬은 하면 안됨
# determination O(N)
# 이분탐색 O(logX), X = 블루레이의 크기, S, 10억
