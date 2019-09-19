cash1 = open('Cash1.txt', 'r')
cash2 = open('Cash2.txt', 'r')
cash3 = open('Cash3.txt', 'r')
cash4 = open('Cash4.txt', 'r')
cash5 = open('Cash5.txt', 'r')
a = [float(i) for i in cash1.readlines()]
b = [float(i) for i in cash2.readlines()]
c = [float(i) for i in cash3.readlines()]
d = [float(i) for i in cash4.readlines()]
e = [float(i) for i in cash5.readlines()]
all_1 = a+b+c+d+e
ind = all_1.index(max(all_1))
if (ind == 0) or (ind == 16) or (ind == 32) or (ind == 48) or (ind == 64): print('Время:', '8:00 - 8:30','\n' 'Интервал: 1')
if (ind - 1 == 0) or (ind - 1 == 16) or (ind - 1 == 32) or (ind - 1 == 48) or (ind - 1 == 64): print('Время:', '8:30 - 9:00','\n' 'Интервал: 2')
if (ind - 2 == 0) or (ind - 2 == 16) or (ind - 2 == 32) or (ind - 2 == 48) or (ind - 2 == 64): print('Время:', '9:00 - 9:30','\n' 'Интервал: 3')
if (ind - 3 == 0) or (ind - 3 == 16) or (ind - 3 == 32) or (ind - 3 == 48) or (ind - 3 == 64): print('Время:', '9:30 - 10:00','\n' 'Интервал: 4')
if (ind - 4 == 0) or (ind - 4 == 16) or (ind - 4 == 32) or (ind - 4 == 48) or (ind - 4 == 64): print('Время:', '10:00 - 10:30','\n' 'Интервал: 5')
if (ind - 5 == 0) or (ind - 5 == 16) or (ind - 5 == 32) or (ind - 5 == 48) or (ind - 5 == 64): print('Время:', '10:30 - 11:00','\n' 'Интервал: 6')
if (ind - 6 == 0) or (ind - 6 == 16) or (ind - 6 == 32) or (ind - 6 == 48) or (ind - 6 == 64): print('Время:', '11:00 - 11:30','\n' 'Интервал: 7')
if (ind - 7 == 0) or (ind - 7 == 16) or (ind - 7 == 32) or (ind - 7 == 48) or (ind - 7 == 64): print('Время:', '11:30 - 12:00','\n' 'Интервал: 8')
if (ind - 8 == 0) or (ind - 8 == 16) or (ind - 8 == 32) or (ind - 8 == 48) or (ind - 8 == 64): print('Время:', '12:00 - 12:30','\n' 'Интервал: 9')
if (ind - 9 == 0) or (ind - 9 == 16) or (ind - 9 == 32) or (ind - 9 == 48) or (ind - 9 == 64): print('Время:', '12:30 - 13:00','\n' 'Интервал: 10')
if (ind - 10 == 0) or (ind - 10 == 16) or (ind - 10 == 32) or (ind - 10 == 48) or (ind - 10 == 64): print('Время:', '13:00 - 13:30','\n' 'Интервал: 11')
if (ind - 11 == 0) or (ind - 11 == 16) or (ind - 11 == 32) or (ind - 11 == 48) or (ind - 11 == 64): print('Время:', '13:30 - 14:00','\n' 'Интервал: 12')
if (ind - 12 == 0) or (ind - 12 == 16) or (ind - 12 == 32) or (ind - 12 == 48) or (ind - 12 == 64): print('Время:', '14:00 - 14:30','\n' 'Интервал: 13')
if (ind - 13 == 0) or (ind - 13 == 16) or (ind - 13 == 32) or (ind - 13 == 48) or (ind - 13 == 64): print('Время:', '14:30 - 15:00','\n' 'Интервал: 14')
if (ind - 14 == 0) or (ind - 14 == 16) or (ind - 14 == 32) or (ind - 14 == 48) or (ind - 14 == 64): print('Время:', '15:00 - 15:30','\n' 'Интервал: 15')
if (ind - 15 == 0) or (ind - 15 == 16) or (ind - 15 == 32) or (ind - 15 == 48) or (ind - 15 == 64): print('Время:', '15:30 - 16:00','\n' 'Интервал: 16')