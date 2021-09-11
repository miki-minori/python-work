#解けなかった#

N=int(input())
S=[]
T=[]
for x in range(N):
    s=list(input())
    S.append(s)
for x in range(N):
    t=list(input())
    T.append(t)

if(S == T):
    print('Yes')
else:
    print('No')