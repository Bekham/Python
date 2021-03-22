class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки. Инструмент: {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки. Инструмент: {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки. Инструмент: {self.title}')


s = Stationery('')
s.draw()
pn = Pen('ручка')
pn.draw()
pl = Pencil('карандаш')
pl.draw()
h = Handle('маркер')
h.draw()
