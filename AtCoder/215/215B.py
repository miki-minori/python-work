## def log2(x, y):
##     if x < y:
##         return 0
##     return 1 + log2(x/y, y)

N=int(input())
## print(log2(N,2))

count = 0
m = 1
while (m <= N):
    m *= 2
    count += 1
print(count-1)
