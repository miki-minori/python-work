import random

def henkan(se):
    if se == 0:
        print('✊')
    elif se == 1:
        print('✌️')
    elif se == 2:
        print('✋')

print('mode select.')
print('nomal:0')
print('easy:1')
mode = int(input())

print('✊ 0 ✌️ 1 ✋ 2  🏃 9')
se1 = 100
se2 = 100

if mode == 0:
    while se1 == se2:
        se1 = 100
        while se1 >= 3:
            se1 = int(input())
            if se1 == 9:
                exit()
        henkan(se1)

        se2 = random.randint(0,2)
        henkan(se2)

        if se1 == se2:
            print('あいこ')
    if (se1 - se2 == -1) or (se1 - se2 == 2):
        print('勝ち')
    else:
        print('負け')

else:
    for i in range(100):
        se1 = 100
        while se1 >= 3:
            se1 = int(input())
            if se1 == 9:
                exit()
        henkan(se1)

        if se1 == 0:
            se2 = 1
        elif se1 == 1:
            se2 = 2
        else:
            se2 = 0
        henkan(se2)
        print('勝ち')
