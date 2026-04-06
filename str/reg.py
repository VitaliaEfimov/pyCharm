import re

n = int(input())
l = [input() for _ in range(n)]
pattern = r'a.*n.*t.*o.*n'

for i in range(len(l)):
    if re.search(pattern, l[i]):
        print(i + 1, end=' ')