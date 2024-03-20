import sys
input = sys.stdin.readline

A, B = input().split()

def char2deci(char):
    if ord(char) >= 97 :
        return ord(char) - 87
    return int(char)

for s in [A, B]:
    for c in s:
        print(char2deci(c))
