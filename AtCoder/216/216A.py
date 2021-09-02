li = list(map(int,input().split('.')))

if(li[1]<3):
    print('%d-'%li[0])
elif(li[1]<7):
    print('%d'%li[0])
else:
    print('%d+'%li[0])