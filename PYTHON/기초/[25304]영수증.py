import sys

input = sys.stdin.readline

x = int(input())
n = int(input())
s = 0
for _ in range(n):
    price, num = map(int, input().split())
    s += price * num

print("Yes" if s == x else "No")
