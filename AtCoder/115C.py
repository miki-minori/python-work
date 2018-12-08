line = input().split(" ")
n = int(line[0])
k = int(line[1])
h = []
sa = 9999999999999999999999


for i in range(n):
    h.append(int(input()))

h = sorted(h)

for i in range(n-k+1):
    if (h[k+i-1] - h[i]) < sa:
        sa = h[k+i-1] - h[i]

print(sa)
