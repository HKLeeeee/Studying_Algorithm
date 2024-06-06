import sys
input = sys.stdin.readline
N, K, P, X = map(int, input().split())
diff = [[0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
        [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
        [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
        [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
        [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
        [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
        [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
        [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
        [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
        [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]]

curr = []
for i in range(K, 0, -1):
    curr.append(X // 10 ** (i-1))
    X = X % 10 ** (i-1)

changed = []
answer = 0
def rec_func(idx, cnt):
    if idx == K:
        result = int(''.join(changed))
        if 0 < result <= N :
            global answer
            answer += 1
            return
        return

    for to in range(10):
        flip_num = diff[curr[idx]][to]
        if cnt + flip_num <= P:
            changed.append(str(to))
            rec_func(idx + 1, cnt + flip_num)
            changed.pop()

rec_func(0, 0)
print(answer - 1)

