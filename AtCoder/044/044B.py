import sys

line = input()
line = list(line)
d = {}

for i in line:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for i in d.values():
    if i % 2 != 0:
        print('No')
        sys.exit()

print('Yes')
