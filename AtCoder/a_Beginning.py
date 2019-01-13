line = [1, 9, 7, 4]
n = input().split(" ")

for i in range(4):
    for j in n:
        if line[i] == int(j):
            line[i] = 0
            break

if sum(line) == 0:
    print("YES")
    exit()

print("NO")
