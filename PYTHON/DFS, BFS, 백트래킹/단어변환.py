from collections import deque


def changable(from_word, to_word):
    cnt = 0
    for (a, b) in zip(from_word, to_word):
        if a != b:
            cnt += 1
        if cnt > 2:
            return False
    return cnt == 1


def solution(begin, target, words):
    if target not in words:
        return 0

    q = deque()
    q.append((begin, 0))
    answer = 0
    visit = [False for _ in range(len(words))]
    while q:
        word, time = q.popleft()
        if word == target:
            answer = time
            break
        for i, w in enumerate(words):
            if not visit[i] and changable(word, w):
                q.append((w, time + 1))

    return answer


begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))