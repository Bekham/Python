import sys


def edit_data(*args):
    """Редактирование значения в списке bakery.csv"""
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if int(args[0]) in range(len(lines)):
        lines[int(args[0]) - 1] = args[1] + '\n'
        with open('bakery.csv', "w") as f:
            f.writelines(lines)
    else:
        print('Введенный номер строки отсутствует')


if __name__ == '__main__':
    try:
        first = sys.argv[1]
    except IndexError:
        first = False
    try:
        num = sys.argv[2]
    except IndexError:
        num = False
    if first and num:
        edit_data(first, num)
