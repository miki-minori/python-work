line = input().split(" ")
N = int(line[0])
L = int(line[1])

str = [0 for i in range(N)]
for i in range(N):
    str[i] = input()

str = sorted(str)
for i in range(N):
    print(''.join(str[i]), end = '')
