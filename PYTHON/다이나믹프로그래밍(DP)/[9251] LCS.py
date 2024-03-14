import sys
input = sys.stdin.readline

# ACAYKP
# CAPCAK
A = input().strip()
B = input().strip()
N = len(B)
visit = [False for _ in range(N)]
ans = 0

for i, a in enumerate(A):
    for j in range(i+1, N):
        if B[j] == A[i] and not visit[i]:
            visit[i] = True
            ans += 1
            break


print(ans)