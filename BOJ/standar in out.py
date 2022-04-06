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


def BS(find, v, start, end):
    if start > end :
        return False
    mid = (start + end) // 2
    if v[mid]==find:
        return True
    elif v[mid]>find:
        return BS(find, v, start, mid-1)
    else :
        return BS(find, v, mid+1, end)


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

    # input = sys.stdin.readline
    #
    # x = int(input())
    #
    # for i in range(x):
    #     call_0 = 0
    #     call_1 = 0
    #     result = fibo(int(input()))
    #     sys.stdout.write(str(call_0)+" "+str(call_1))
    input = sys.stdin.readline
    print = sys.stdout.write

    # n = int(input())
    # first = sorted(list(map(int, input().split())))
    # n = int(input())
    # second = list(map(int, input().split()))
    # for i in second:
    #     if BS(i, first, 0, len(first) - 1):
    #         print('1\n')
    #     else:
    #         print('0\n')

    # from collections import defaultdict
    #
    # n = int(input())
    # dic = defaultdict(int)
    # lst = sorted(list(map(int, input().split())))
    # for i in lst:
    #     dic[i] += 1
    # n = int(input())
    # find = list(map(int, input().split()))
    # for i in find:
    #     print('{} '.format(dic[i]))

    n = int(input())
    dic = {}
    lst = sorted(list(map(int, input().split())))
    for i in lst:
        if dic.get(i) is None:
            dic[i] = 1
        else:
            dic[i] += 1

    n = int(input())
    find = list(map(int, input().split()))
    for i in find:
        if dic.get(i) is None:
            print('0 ')
        else:
            print('{} '.format(dic[i]))