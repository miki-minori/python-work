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

def hantei(gamen,x):
    if (gamen[0][0] == x) and (gamen[0][1] == x) and (gamen[0][2] == x):
        return True
    elif (gamen[1][0] == x) and (gamen[1][1] == x) and (gamen[1][2] == x):
        return True
    elif (gamen[2][0] == x) and (gamen[2][1] == x) and (gamen[2][2] == x):
        return True
    elif (gamen[0][0] == x) and (gamen[1][0] == x) and (gamen[2][0] == x):
        return True
    elif (gamen[0][1] == x) and (gamen[1][1] == x) and (gamen[2][1] == x):
        return True
    elif (gamen[0][2] == x) and (gamen[1][2] == x) and (gamen[2][2] == x):
        return True
    elif (gamen[0][0] == x) and (gamen[1][1] == x) and (gamen[2][2] == x):
        return True
    elif (gamen[0][2] == x) and (gamen[1][1] == x) and (gamen[2][1] == x):
        return True
    else:
        return False

print('mode select.')
print('1人:0')
print('2人:1')

se = 10
while (se != 0) or (se != 1):
    se = int(input())
    hyouji()
    if se == 0:

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

            if hantei(gamen,'〇') == True:
                print('〇の勝ち')
                break
            elif hantei(gamen,'✖') == True:
                print('✖の勝ち')
                break
        print('終了')
        break

    elif se == 1:
        for num in range(9):
            line = input().split(" ")
            n = int(line[0])
            m = int(line[1])
            while (n >= 3) or (m >= 3) or (gamen[n][m] != '＊'):
                line = input().split(" ")
                n = int(line[0])
                m = int(line[1])
            if num % 2 == 0:
                gamen[n][m] = '〇'
            else:
                gamen[n][m] = '✖'
            hyouji()

            if hantei(gamen,'〇') == True:
                print('〇の勝ち')
                break
            elif hantei(gamen,'✖') == True:
                print('✖の勝ち')
                break
        print('終了')
        break
