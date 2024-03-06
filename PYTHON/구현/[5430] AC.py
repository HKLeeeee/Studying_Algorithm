import sys
import re

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    func = input().strip()
    n = int(input())
    lst_str = input().strip()
    lst = re.findall(r'\d+', lst_str)
    if func.count("D") > len(lst):
        print('error')
        continue

    direction = True
    L, R = 0, n
    for f in func:
        if f == "R":
            direction = not direction
        elif f == "D":
            if direction:
                L += 1
            else:
                R -= 1

    if direction:
        print("[" + ','.join(lst[L:R]) + "]")
    else:
        temp = lst[L:R]
        print("[" + ','.join(temp[::-1]) + "]")
