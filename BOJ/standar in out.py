import sys

def vps(ps):
    stack = []

    for v in ps :
        if v == "(" or v == "[":
            stack.append(v)
        elif v == ")":
            if len(stack) == 0 :
                return False
            else :
                if stack[-1] == "(" :
                    stack.pop()
                else :
                    return False
        elif v == "]":
            if len(stack) == 0 :
                return False
            else :
                if stack[-1] == "[" :
                    stack.pop()
                else :
                    return False

    if len(stack) != 0 :
        print(3)
        return False

    return True


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

    while True:
        t = sys.stdin.readline()
        if t == ".\n" or t == ".":
            break
        print("yes" if vps(t) else "no")
