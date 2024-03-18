N, K = map(int, input().split())
prime = [True] * (N + 1)

def eratosthenes() :
    cnt = 0
    for i in range(2, N+1):
        for j in range(i, N+1, i):
            if prime[j]:
                prime[j] = False
                cnt += 1
                if cnt == K :
                    print(j)
                    return

eratosthenes()