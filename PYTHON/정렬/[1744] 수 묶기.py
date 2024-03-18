import sys
input = sys.stdin.readline

N = int(input())
pos = []
neg = []
zero = False
for _ in range(N):
    n = int(input())
    if n > 0:
        pos.append(n)
    elif n == 0:
        zero = True
    else:
        neg.append(n)

pos.sort(reverse=True)
neg.sort()

ans = 0
idx = 0
while idx < len(pos):
    if idx + 1 < len(pos):
        if pos[idx] * pos[idx + 1] > pos[idx] + pos[idx + 1]:
            ans += pos[idx] * pos[idx + 1]
            idx += 2
        else:
            ans += pos[idx]
            idx += 1
    else:
        ans += pos[idx]
        idx += 1

if len(neg) % 2 != 0 and zero:
    neg.pop()

idx = 0
while idx < len(neg):
    if idx + 1 < len(neg):
        ans += neg[idx] * neg[idx + 1]
        idx += 2
    else :
        ans += neg[idx]
        idx += 1

print(ans)