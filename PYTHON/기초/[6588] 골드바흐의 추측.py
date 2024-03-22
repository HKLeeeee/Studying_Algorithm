import sys
input = sys.stdin.readline
N = 1000001

def prime_list():
    prime = [True for _ in range(N)]
    prime[0] = False
    prime[1] = False

    for i in range(2, int(N ** 0.5) + 1):
        if not prime[i]:
            continue
        for j in range(i + i, N, i):
            prime[j] = False
    return prime


PRIME = prime_list()

while True:
    n = int(input())
    if n == 0:
        break
    a, b = 0, 0
    diff = -1
    for i in range(n // 2 + 1):
        if PRIME[i] and PRIME[n - i]:
            if diff == -1:
                diff = n - i - i
                a = i
                b = n - i
                break
    if diff == -1:
        print("Goldbach's conjecture is wrong.")
    else:
        print(f"{n} = {a} + {b}")
