l = input().split()
r = [[]]

for i in range(1, len(l) + 1):
    for j in range(len(l)):
        if j + i <= len(l):
            print(j, j+i)
            r.append(l[j:j+i])

print(r)