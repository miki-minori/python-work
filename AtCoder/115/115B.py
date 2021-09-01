n = int(input())
list = []
max = 0
ans = 0

for i in range(n):
    line = int(input())
    list.append(line)
    if list[i] > max:
        max = list[i]
        c = i

for i in range(n):
    if c == i:
        ans = ans + (list[i] / 2)
    else:
        ans = ans + list[i]

print(int(ans))
