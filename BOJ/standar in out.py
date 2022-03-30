import sys


def vps(ps):
    stack = []

    for v in ps:
        if v == "(" or v == "[":
            stack.append(v)
        elif v == ")":
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
        elif v == "]":
            if len(stack) == 0:
                return False
            else:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False

    if len(stack) != 0:
        print(3)
        return False

    return True


def fibo(n):
    global call_0
    global call_1
    if n == 0:
        call_0 += 1
        return n
    elif n == 1:
        call_1 += 1
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


if __name__ == '__main__':
    # n = int(sys.stdin.readline())
    #
    # lst = list(map(int, sys.stdin.readline().split()))
    #
    # num = list(set(lst))
    # num.sort()
    #
    # for x in lst:
    #     sys.stdout.write(str(num.index(x)) + " ")
    #
    # while True:
    #     t = sys.stdin.readline()
    #     if t == ".\n" or t == ".":
    #         break
    #     print("yes" if vps(t) else "no")

    input = sys.stdin.readline

    x = int(input())

    for i in range(x):
        call_0 = 0
        call_1 = 0
        result = fibo(int(input()))
        sys.stdout.write(str(call_0)+" "+str(call_1))
