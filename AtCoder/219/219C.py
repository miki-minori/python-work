def f(x):
    s=[]
    x=list(x)
    for i in x:
        s.append(Xd[i])
    return s

X=list(input())
Xd={}
for i in range(26):
    Xd[X[i]]=i

N=int(input())
S=[]
for _ in range(N):
    s=input()
    S.append(s)

S.sort(key=f)

for i in S:
    print(i)