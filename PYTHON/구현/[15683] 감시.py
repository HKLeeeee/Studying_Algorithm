import sys
import copy

input = sys.stdin.readline

N, M = map(int, input().split())
office = []
cctv = []  # (x, y, type)
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 오, 왼, 위, 아래
cctv_dir = {
    1: [[d[0]], [d[1]], [d[2]], [d[3]]],
    2: [[d[0], d[1]], [d[2], d[3]]],
    3: [[d[0], d[2]], [d[0], d[3]], [d[1], d[2]], [d[1], d[3]]],
    4: [[d[0], d[1], d[2]], [d[0], d[1], d[3]], [d[1], d[2], d[3]], [d[0], d[2], d[3]]],
    5: [d]
}

for i in range(N):
    line = list(map(int, input().split()))
    for j, l in enumerate(line):
        if l != 0 and l != 6:
            cctv.append((i, j, l))
    office.append(line)


def check(dir_list):  # [(x,y,dir_list)]
    this_office = copy.deepcopy(office)
    # move
    for info in dir_list:
        x, y, dirs = info
        for d in dirs:
            nx, ny = x, y
            while 0 <= nx < N and 0 <= ny < M:
                if this_office[nx][ny] == 0:
                    this_office[nx][ny] = "#"
                elif this_office[nx][ny] == 6:
                    break
                nx, ny = nx + d[0], ny + d[1]
    # count
    cnt = 0
    for off in this_office:
        for o in off:
            if o == 0:
                cnt += 1
    return cnt


def ref_func(dir_list, cctv_idx):
    if len(dir_list) == len(cctv):
        return check(dir_list)

    x, y, cctv_type = cctv[cctv_idx]
    ans = 65
    for dir in cctv_dir[cctv_type]:
        dir_list.append((x, y, dir))
        ans = min(ans, ref_func(dir_list, cctv_idx+1))
        dir_list.pop()

    return ans

print(ref_func([], 0))