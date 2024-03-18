from collections import deque
N, K = map(int, input().split())
q = deque([i+1 for i in range(N)])
order = []
while q:
    for _ in range(K-1):
        q.append(q.popleft())
    order.append(str(q.popleft()))


print("<" + ", ".join(order) + ">")