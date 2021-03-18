class CalcError(Exception):
    pass


def val_checker(x):
    def type_logger(func):
        def wrapper(*args):
            nonlocal x
            if x(*args):

                result = func(*args)
                print(f'call {func.__name__}({", ".join(map(str, args))}:{type(args)} = {result}:{type(result)}),')
                return result
            else:
                print(f'wrong val: {", ".join(map(str, args))}')
                raise CalcError

        return wrapper

    return type_logger


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(-5)
