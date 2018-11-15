import random

place = [[99 for w in range(10)] for h in range(2)]

for h in range(2):
    for w in range(10):
        place[h][w] = w
        print('□', end = '')
    random.shuffle(place[h])
    print()

print(place)
player = [20,0,0]
i = 0
for num in range(100):
    i += 1
    if i == 1:
        print('-------------------------------')
        print('A者')
        print(player[1],'枚')
        print('-------------------------------')
    elif i == 2:
        print('-------------------------------')
        print('B者')
        print(player[2],'枚')
        print('-------------------------------')
    else:
        i = 0
    select = [[99, 99], [99, 99]]
    for count in range(2):
        while (select[count][0] > 1) or (select[count][1] > 9) or (place[select[count][0]][select[count][1]] == 99):
            print()
            sel = input().split(" ")
            select[count][0] = int(sel[0])
            select[count][1] = int(sel[1])

        for h in range(2):
            for w in range(10):
                if (h == select[count][0]) and (w == select[count][1]):
                    print(place[h][w], '', end = '')
                elif (h == select[count-1][0]) and (w == select[count-1][1]):
                    print(place[h][w], '', end = '')
                else:
                    if place[h][w] != 99:
                        print('□', end = '')
                    else:
                        print('　', end = '')
            print()

    if (place[select[0][0]][select[0][1]]) == (place[select[1][0]][select[1][1]]):
        place[select[0][0]][select[0][1]] = 99
        place[select[1][0]][select[1][1]] = 99
        player[i] += 2
        player[0] -= 2
        i -= 1

    if player[0] == 0:
        print('A者',player[1],'枚','B者',player[2],'枚')
        break
