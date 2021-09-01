n = int(input())
t = []
sum = 0

line = input().split(" ")
for i in range(n):
    t.append(int(line[i]))
    sum += int(line[i])

m = int(input())
for i in range(m):
    line = input().split(" ")
    p = int(line[0]) - 1
    x = int(line[1])
    for j in range(len(t)):
        if j == p:
            comp = sum - t[j] + x
    print(comp)
