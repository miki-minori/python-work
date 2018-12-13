n = int(input())
s = input()
line = list(s)
x = 0
xmax = 0

for i in range(n):
    if line[i] == 'I':
        x += 1
        if xmax < x:
            xmax = x
    elif line[i] == 'D':
        x -= 1

print(xmax)
