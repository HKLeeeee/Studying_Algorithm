import sys
input = sys.stdin.readline
def roundUp(x):
    if x * 10 % 10 >= 5:
        return int(x) + 1
    else :
        return int(x)

n = int(input())
score = [int(input()) for _ in range(n)]
if n == 0:
    print(0)
    exit(0)
remove = roundUp(n * 0.15)
score.sort()
score = score[remove:n - remove]
print(roundUp(sum(score) / (n - 2 * remove)))