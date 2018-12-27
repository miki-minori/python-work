import math
n = int(input())
val = math.factorial(n)
ans = val % (10**9 + 7)

print(ans)
