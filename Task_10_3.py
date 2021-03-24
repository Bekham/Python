class OrganicCell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return f'{self.cell + other.cell}'

    def __sub__(self, other):
        return [f'{self.cell - other.cell}' if (self.cell - other.cell) >= 0 else f'Error! Difference less than 0'][0]

    def __mul__(self, other):
        return f'{self.cell * other.cell}'

    def __floordiv__(self, other):
        return f'{self.cell // other.cell}'

    def make_order(self, n):
        int_rows = self.cell // n
        mass = ''
        for i in range(1, int_rows + 1):
            mass += '*' * n + '\n'
        if self.cell % n != 0:
            mass += '*' * (self.cell - n * int_rows) + '\n'
        return mass


o_1 = OrganicCell(12)
o_2 = OrganicCell(9)
print(f'o_1.cell: {o_1.cell}')
print(f'o_2.cell: {o_2.cell}')
print(f'__add__: {o_1 + o_2}')
print(f'__sub__: {o_1 - o_2}')
print(f'__mul__: {o_1 * o_2}')
print(f'__floordiv__: {o_1 // o_2}')
print(f'make_order:\n{o_1.make_order(5)}')
