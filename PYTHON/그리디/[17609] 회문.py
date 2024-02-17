import sys
input = sys.stdin.readline
N = int(input())
str = [input().strip() for _ in range(N)]

def palindrome(s):
    L, R = 0, len(s) - 1
    while L < R:
        print(L, R, s[L], s[R])
        if s[L] == s[R]:
            L += 1
            R -= 1

        else:
            if R - L >= 1:
                temp = s[:L] + s[L + 1:]
                if temp[:] == temp[::-1]:
                    return 1

                temp = s[:R] + s[R + 1:]
                if temp[:] == temp[::-1]:
                    return 1
            return 2
    return 0

for s in str:
    print(palindrome(s))
