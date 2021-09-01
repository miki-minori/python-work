line = input().split(" ")
n = int(line[0])
m = int(line[1])
a = []
b = []

for i in range(n):
    a.append(input())
for i in range(m):
    b.append(input())

for nh in range(n-m+1):
    for nw in range(n-m+1):
        for k in range(m):
            s1 = a[nh+k][nw : nw+m]
            s2 = b[k]
            if s1 != s2:
                break
        else:
            print("Yes")
            exit()

print("No")
