N = int(input())
students = [list(input().split()) for _ in range(N)]
result = sorted(students, key=lambda x: (-1 * int(x[1]), int(x[2]), -1*int(x[3]), x[0]))

for s in result:
    print(s[0])
