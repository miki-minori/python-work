N=int(input())
li=[input() for i in range(N)]

if(len(li)==len(set(li))):
    print('No')
else:
    print('Yes')