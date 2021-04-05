class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def is_number(inp_str):
        try:
            float(inp_str)
            return True
        except ValueError:
            return False


stop = False
nums = []
while not stop:
    inp_data = input('Введите новое значение для списка: ')
    try:
        if inp_data == 'stop':
            stop = True
        if not OwnError.is_number(inp_data):
            raise OwnError('Необходимо ввести число!')
    except OwnError as err:
        print(err)
    except Exception as err:
        print(err)
    else:
        nums.append(float(inp_data))
print(nums)
