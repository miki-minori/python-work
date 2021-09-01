linea = input()
linea = list(linea)
lineb = input()
lineb = list(lineb)
linec = input()
linec = list(linec)
line = []

line.append(linea)
line.append(lineb)
line.append(linec)

c = 0
for i in range(300):
    if len(line[c]) != 0:
        if line[c][0] == 'a':
            del line[c][0]
            c = 0
        elif line[c][0] == 'b':
            del line[c][0]
            c = 1
        elif line[c][0] == 'c':
            del line[c][0]
            c = 2
    else:
        if c == 0:
            print('A', end='')
        elif c == 1:
            print('B', end='')
        elif c == 2:
            print('C', end='')
        exit()
