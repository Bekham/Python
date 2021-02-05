import random

print ('Загадайте число от 1 до 100')
range_min = 0
range_max = 101
win = False
while win == False:
    number = int(range_min+(range_max-range_min)/2)
    print ('Если компьютер угадал, введите 1')
    print ('Если компьютер не угадал, и Ваше число больше - введите >')
    print ('Если компьютер не угадал, и Ваше число меньше - введите <')
    answer = input(f'Ваше загаданное число: {number} ?')

    if answer == '1':
        win = True
    elif answer == '<':
        range_max = number
    else:
        range_min = number
    print(range_min, range_max)
if win == True:
    print(f'Вы загадали число: {answer}. Ура. Компьютер угадал.')