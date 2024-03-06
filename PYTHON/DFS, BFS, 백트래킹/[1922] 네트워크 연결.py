# Union-Find 자료구조를 구현합니다.
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

# Kruskal 알고리즘을 이용하여 최소 스패닝 트리를 찾습니다.
def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # 가중치에 따라 간선을 정렬합니다.
    uf = UnionFind(n)
    mst_cost = 0
    mst_edges = []

    for edge in edges:
        u, v, weight = edge
        if uf.union(u, v):
            mst_cost += weight
            mst_edges.append(edge)

    return mst_cost

if __name__ == "__main__":
    n = int(input())  # 정점의 개수
    m = int(input())  # 간선의 개수

    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())  # a와 b를 연결하는 가중치 c의 간선
        edges.append((a - 1, b - 1, c))  # 정점 번호를 0부터 시작하도록 조정합니다.

    min_cost = kruskal(n, edges)
    print(min_cost)
