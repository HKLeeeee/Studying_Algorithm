import sys
from collections import defaultdict
input = sys.stdin.readline

def convert2num(s) :
    result = ''
    for c in s:
        result += alphabet_value[c]
    return int(result)

n = int(input())
lst = [input().strip() for _ in range(n)]
alphabet = defaultdict(int)
alphabet_value = {}
for l in lst:
    str_len = len(l)
    for i, alpha in enumerate(l):
        alphabet[alpha] += 10 ** (str_len - i)

result = sorted(alphabet.items(), key=lambda x : x[1], reverse=True)
for i, (a, v) in enumerate(result):
    alphabet_value[a] = str(9 - i)

lst = list(map(convert2num, lst))
print(sum(lst))