line = input()
str = list(line)
ans = []
c = 0

for i in str:
    if (i == "1") or (i == "0"):
        ans.append(i)
    elif i == "B":
        if c != 0:
            c -= 1
            del ans[c]
        c -= 1
    c += 1

for i in ans:
    print("".join(i), end = '')
