import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
files = [input().strip().split(".")[1] for _ in range(N)]
counter = Counter(files)
result = sorted(counter.items(), key=lambda x: x[0])
for r in result:
    print(*r)
