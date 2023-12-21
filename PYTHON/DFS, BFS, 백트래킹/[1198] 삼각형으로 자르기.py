N = int(input())
dots = [list(map(int, input().split())) for _ in range(N)]
selected = []
max_ = 0


def triangle_area(x, y, z):
    return abs((x[0] * y[1] + y[0] * z[1] + z[0] * x[1]) - (x[1] * y[0] + y[1] * z[0] + z[1] * x[0])) / 2


def ref_func(k, idx):
    global max_
    if k == 3:
        max_ = max(max_, triangle_area(*selected))
    else:
        for i in range(idx, len(dots)):
            selected.append(dots[i])
            ref_func(k + 1, i + 1)
            selected.pop()


ref_func(0, 0)
print(max_)
