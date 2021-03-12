import sys


def write_data(num):
    """Добавление новых значений в конец списка bakery.csv"""
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(num + '\n')


if __name__ == '__main__':
    if sys.argv[1]:
        write_data(sys.argv[1])
