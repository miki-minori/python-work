line = input().split(" ")
k = int(line[0])
s = int(line[1])
count = 0

for x in range(0, k+1, 1):
    for y in range(0, k+1, 1):
        z = s - x - y
        if 0 <= z and z <= k:
            count += 1

print(count)
