import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = []
a, b = 0, 0
while a < N and b < M :
    if A[a] >= B[b]:
        ans.append(B[b])
        b += 1
    else :
        ans.append(A[a])
        a += 1

while a < N :
    ans.append(A[a])
    a+= 1

while b < M :
    ans.append(B[b])
    b += 1

print(*ans)