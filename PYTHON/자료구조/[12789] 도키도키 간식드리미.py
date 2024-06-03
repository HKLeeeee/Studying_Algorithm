N = int(input())
students = list(map(int, input().split()))
wait_line = []
curr = 0
idx = 0
while curr < N:
    if idx < N and students[idx] - 1 == curr:
        idx += 1
        curr += 1
    elif len(wait_line) > 0 and wait_line[-1] - 1 == curr:
        wait_line.pop()
        curr += 1
    elif len(wait_line) > 0 and idx < N and wait_line[-1] <= students[idx]:
        print("Sad")
        exit(0)
    else:
        wait_line.append(students[idx])
        idx += 1

print('Nice')