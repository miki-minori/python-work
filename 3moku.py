import random

gamen = [['＊','＊','＊'],['＊','＊','＊'],['＊','＊','＊']]
print()

def hyouji():
    for i in gamen:
        for j in i:
            print(j,end="")
            print('|',end="")
        print()
        print('---------')

hyouji()

for num in range(9):
    if num %2 == 0:
        line = input().split(" ")
        n = int(line[0])
        m = int(line[1])
        while (n >= 3) or (m >= 3) or (gamen[n][m] != '＊'):
            line = input().split(" ")
            n = int(line[0])
            m = int(line[1])
        gamen[n][m] = '〇'
    else:
        n = random.randint(0,2)
        m = random.randint(0,2)
        while (n >= 3) or (m >= 3) or (gamen[n][m] != '＊'):
            n = random.randint(0,2)
            m = random.randint(0,2)
        gamen[n][m] = '✖'
    hyouji()
    print()

    if (gamen[0][0] == '〇') and (gamen[0][1] == '〇') and (gamen[0][2] == '〇'):
        print('〇の勝ち')
        break
    elif (gamen[0][0] == '✖') and (gamen[0][1] == '✖') and (gamen[0][2] == '✖'):
        print('✖の勝ち')
        break
    elif (gamen[1][0] == '〇') and (gamen[1][1] == '〇') and (gamen[1][2] == '〇'):
        print('〇の勝ち')
        break
    elif (gamen[1][0] == '✖') and (gamen[1][1] == '✖') and (gamen[1][2] == '✖'):
        print('✖の勝ち')
        break
    elif (gamen[2][0] == '〇') and (gamen[2][1] == '〇') and (gamen[2][2] == '〇'):
        print('〇の勝ち')
        break
    elif (gamen[2][0] == '✖') and (gamen[2][1] == '✖') and (gamen[2][2] == '✖'):
        print('✖の勝ち')
        break
    elif (gamen[0][0] == '〇') and (gamen[1][0] == '〇') and (gamen[2][0] == '〇'):
        print('〇の勝ち')
        break
    elif (gamen[0][0] == '✖') and (gamen[1][0] == '✖') and (gamen[2][0] == '✖'):
        print('✖の勝ち')
        break
    elif (gamen[0][1] == '〇') and (gamen[1][1] == '〇') and (gamen[2][1] == '〇'):
        print('〇の勝ち')
        break
    elif (gamen[0][1] == '✖') and (gamen[1][1] == '✖') and (gamen[2][1] == '✖'):
        print('✖の勝ち')
        break
    elif (gamen[0][2] == '〇') and (gamen[1][2] == '〇') and (gamen[2][2] == '〇'):
        print('〇の勝ち')
        break
    elif (gamen[0][2] == '✖') and (gamen[1][2] == '✖') and (gamen[2][2] == '✖'):
        print('✖の勝ち')
        break
    elif (gamen[0][0] == '〇') and (gamen[1][1] == '〇') and (gamen[2][2] == '〇'):
        print('〇の勝ち')
        break
    elif (gamen[0][0] == '✖') and (gamen[1][1] == '✖') and (gamen[2][2] == '✖'):
        print('✖の勝ち')
        break
    elif (gamen[0][2] == '〇') and (gamen[1][1] == '〇') and (gamen[2][1] == '〇'):
        print('〇の勝ち')
        break
    elif (gamen[0][2] == '✖') and (gamen[1][1] == '✖') and (gamen[2][1] == '✖'):
        print('✖の勝ち')
        break

print('終了')
