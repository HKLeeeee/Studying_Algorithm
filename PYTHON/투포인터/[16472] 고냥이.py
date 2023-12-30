import sys

input = sys.stdin.readline

N = int(input())
s = input().strip()
count = [0 for i in range(26)]

unique = 0
L, R = 0, 0
ans = 0
while R < len(s):
    if count[ord(s[R]) - 97] == 0:
        unique += 1
    count[ord(s[R]) - 97] += 1
    R += 1
    while unique > N:
        count[ord(s[L]) - 97] -= 1
        if count[ord(s[L]) - 97] == 0:
            unique -= 1
        L += 1

    ans = max(ans, R - L)

print(ans)

