import sys
input = sys.stdin.readline

N = int(input())
stack = [0 for _ in range(N)]
pointer = 0
for _ in range(N):
    order = input().split()
    if order[0] == '1':
        stack[pointer] = order[1]
        pointer += 1
    elif order[0] == '2':
        if pointer > 0 :
            pointer -= 1
            print(stack[pointer])
        else:
            print(-1)
    elif order[0] == '3':
        print(pointer)
    elif order[0] == '4':
        print(0 if pointer > 0 else 1)
    elif order[0] == '5':
        if pointer > 0 :
            print(stack[pointer-1])
        else :
            print(-1)