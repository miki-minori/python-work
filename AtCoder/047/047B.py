line = input().split(" ")
w = int(line[0])
h = int(line[1])
n = int(line[2])
area = [[0 for wx in range(w)] for hy in range(h)]
c = 0

for i in range(n):
    line = input().split(" ")
    x = int(line[0])
    y = int(line[1])
    a = int(line[2])
    if a == 1:
        for xi in range(h):
            for yi in range(x):
                area[xi][yi] = 1
    elif a == 2:
        for xi in range(h):
            for yi in range(w-x):
                area[xi][yi+x] = 1
    elif a == 3:
        for yi in range(w):
            for xi in range(y):
                area[xi][yi] = 1
    elif a == 4:
        for yi in range(w):
            for xi in range(h-y):
                area[xi+y][yi] = 1

for i in range(h):
    c = area[i].count(0) + c
print(c)
