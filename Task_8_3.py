def logger(verbosity=0):
    def type_logger(func):
        def wrapper(*args, **kwargs):
            result = []
            if verbosity > 0:
                for arg in args:
                    cube = func(arg)
                    result.append(cube)
                    print(f'call {func.__name__}({arg}:{type(arg)} = {cube}:{type(result)}),')
                for key, item in kwargs.items():
                    cube = func(item)
                    result.append(cube)
                    print(f'call {func.__name__}({key} = {item}:{type(kwargs)}) = {cube}:{type(result)},')
            return result

        return wrapper

    return type_logger


@logger(1)
def calc_cube(x):
    return x ** 3


a = calc_cube(3, x=5.7, y=10)
print(*a)
