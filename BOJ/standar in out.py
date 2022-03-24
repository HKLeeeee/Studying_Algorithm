import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())

    lst = list(map(int, sys.stdin.readline().split()))

    num = list(set(lst))
    num.sort()

    for x in lst:
        sys.stdout.write(str(num.index(x)) + " ")


