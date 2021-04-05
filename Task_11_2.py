class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input('Введите уравнение деления (X/Y):')

try:
    if int(inp_data.split('/')[1]) == 0:
        raise OwnError("Вы ввели нулевое значение в знаменателе. На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
except Exception as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {round(int(inp_data.split('/')[0]) / int(inp_data.split('/')[1]), 2)}")
