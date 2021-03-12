import sys


def read_all_data():
    """Чтение всех значений списка bakery.csv"""
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')


def read_slice(*args):
    """Чтение отрезков списка bakery.csv"""
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        if len(args) == 1:
            count = 0
            for line in f:
                count += 1
                if count >= int(args[0]):
                    print(line, end='')
        if len(args) == 2:
            count = 0
            for line in f:
                count += 1
                if int(args[0]) <= count <= int(args[1]):
                    print(line, end='')


if __name__ == '__main__':
    try:
        first = sys.argv[1]
    except IndexError:
        first = False
    try:
        second = sys.argv[2]
    except IndexError:
        second = False
    if first and second:
        read_slice(first, second)
    elif first:
        read_slice(first)
    else:
        read_all_data()
