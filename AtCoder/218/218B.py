P = list(map(int,input().split()))	
num2alpha = lambda c: chr(c+96)

for n in P:
    print(num2alpha(n), end="")