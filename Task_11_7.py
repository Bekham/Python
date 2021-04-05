class ComplexNum:
    def __init__(self, complex_):
        self.complex = complex_
        a, b = 0, 0
        if complex_.endswith('i'):
            if complex_[1:].find('+') != -1:
                a = complex_[:complex_[1:].find('+') + 1]
                if not complex_[complex_.find(a) + len(a) + 1:complex_.find('i')]:
                    b = 1
                    print(b)
                else:
                    b = complex_[complex_.find(a) + len(a):complex_.find('i')]
            elif complex_[1:].find('-') != -1:
                a = complex_[:complex_[1:].find('-') + 1]
                if not complex_[complex_.find(a) + len(a) + 1:complex_.find('i')]:
                    b = -1
                else:
                    b = complex_[complex_.find(a) + len(a):complex_.find('i')]
            else:
                a = 0
                b = complex_[:complex_.find('i')]
        elif not complex_.endswith('i'):
            a = complex_
            b = 0
        self.a = a
        self.b = b

    def __add__(self, other):
        add_a = int(self.a) + int(other.a)
        add_b = int(self.b) + int(other.b)
        if add_b > 0:
            return f'{add_a}+{add_b}i'
        elif add_b < 0:
            return f'{add_a}{add_b}i'
        else:
            return f'{add_a}'

    def __mul__(self, other):
        mul_a = int(self.a)*int(other.a)-int(self.b)*int(other.b)
        mul_b = int(self.a)*int(other.b)+int(self.b)*int(other.a)
        if mul_b > 0:
            return f'{mul_a}+{mul_b}i'
        elif mul_b < 0:
            return f'{mul_a}{mul_b}i'
        else:
            return f'{mul_a}'


first = ComplexNum('-1+9i')
second = ComplexNum('-4i')
print(f'Sum: {first + second}')
print(f'Mul: {first * second}')

