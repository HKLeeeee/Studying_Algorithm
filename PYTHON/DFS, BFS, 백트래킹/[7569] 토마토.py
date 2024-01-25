import sys
from collections import deque
input = sys.stdin.readline

def get_max(three_dimension_list):
    candi = []
    for two in three_dimension_list:
        for one in two:
            candi.append(max(one))
    return max(candi)

def bfs():
    while q:
        h, n, m = q.popleft()
        for dh, dn, dm in direction:
            nh = h + dh
            nn = n + dn
            nm = m + dm
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and boxes[nh][nn][nm] == 0:
                q.append((nh, nn, nm))
                boxes[nh][nn][nm] = boxes[h][n][m] + 1
    for h in range(H):
        for j in range(N):
            for i in range(M):
                if boxes[h][j][i] == 0:
                    return -1
    max_ = get_max(boxes)
    return max_ - 1


M, N, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
direction = [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]
q = deque()

for h in range(H):
    for j in range(N):
        for i in range(M):
            if boxes[h][j][i] == 1:
                q.append((h, j, i))
print(bfs())
