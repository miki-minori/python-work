s = list(input())
min = 200000
max = 0

for i in range(len(s)):
    if s[i] == 'A':
        if min > i:
            min = i
    if s[-i] == 'Z' and i != 0:
        if max < len(s) - i:
            max = len(s) - i

print(max-min+1)
