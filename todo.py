print('list:表示　add:追加　done:タスク完了　clear:完了タスク消去')

todolist = []

line = input()
if line == 'list':
    with open('text.csv',encoding='utf-8') as f:
        for row in f:
            data = row.rstrip().split(',')
            title = data[0]
            yn = int(data[1])
            if yn == 0:
                print('〇',end='')
            elif yn == 1:
                print('●',end='')
            print(title)

elif line == 'add':
    with open('text.csv',mode='a',encoding='utf-8') as f:
        title = input()
        f.write(title)
        f.write(',0')

elif line == 'done':
    with open('text.csv',encoding='utf-8') as f:
        for row in f:
            data = row.rstrip().split(',')
            todolist.append(data)
            if int(data[1]) != 1:
                print(data[0])
        title = input()
        for row in todolist:
            if title == row[0]:
                row[1] = '1'
    with open('text.csv',mode='w',encoding='utf-8') as f:
        for row in todolist:
            title = row[0]
            yn = row[1]
            f.write(title + ',')
            f.write(yn + '\n')

elif line == 'clear':
    with open('text.csv',encoding='utf-8') as f:
        for row in f:
            data = row.rstrip().split(',')
            if int(data[1]) != 1:
                todolist.append(data)
    with open('text.csv',mode='w',encoding='utf-8') as f:
        for row in todolist:
            title = row[0]
            yn = row[1]
            f.write(title + ',')
            f.write(yn + '\n')
