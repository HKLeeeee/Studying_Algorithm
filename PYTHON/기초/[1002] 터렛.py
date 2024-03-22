T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        continue
    if d < r1 + r2:  # 포함
        large = max(r1, r2)
        small = min(r1, r2)
        if d == large - small:  # 내접
            print(1)
        elif d < large - small: # 포함
            print(0)
        else:
            print(2)
    elif d == r1 + r2:  # 접함
        print(1)
    else:  # 외부
        print(0)
