s = input()

for i in range(7, -1, -1):
    j = -(7 - i)
    if s[:i]+s[j:] == "keyence":
        print("YES")
        exit()
print("NO")
