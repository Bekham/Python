class Stock:
    @staticmethod
    def add_item(kind, *params, **kwargs):
        if OfficeEquipment.add_item(kind):
            OfficeEquipment(kind, *params, **kwargs)


class OfficeEquipment:
    pos = ['printer', 'copier', 'scanner']
    office_base = {}

    def __init__(self, kind, quantity, model, cost, year, **kwargs):
        self.kind = kind
        try:
            self.quantity = int(quantity)
        except ValueError:
            print(f'Quantity of {kind} model {model} must be a number!')
            quantity = 0
            self.quantity = quantity
        self.model = model
        self.cost = cost
        self.year = year
        if OfficeEquipment.office_base.get(kind):
            OfficeEquipment.office_base[kind] += quantity
        else:
            OfficeEquipment.office_base[kind] = quantity
        print(f'Add {kind} model {model} to OfficeEquipment base - {quantity} elements')
        if kind == 'printer':
            Printer.printer_params(model, cost, year, **kwargs)
        if kind == 'scanner':
            Scanner.scanner_params(model, cost, year, **kwargs)
        if kind == 'copier':
            Copier.copier_params(model, cost, year, **kwargs)

    @staticmethod
    def add_item(kind):
        if kind in OfficeEquipment.pos:
            return True


class Printer(OfficeEquipment):
    printer_base = {}

    @staticmethod
    def printer_params(model, cost, year, **kwargs):
        printer_el = {'cost': cost, 'year': year}
        for el, num in kwargs.items():
            printer_el[el] = num
        Printer.printer_base[model] = printer_el


class Scanner(OfficeEquipment):
    scanner_base = {}

    @staticmethod
    def scanner_params(model, cost, year, **kwargs):
        scanner_el = {'cost': cost, 'year': year}
        for el, num in kwargs.items():
            scanner_el[el] = num
        Scanner.scanner_base[model] = scanner_el


class Copier(OfficeEquipment):
    copier_base = {}

    @staticmethod
    def copier_params(model, cost, year, **kwargs):
        copier_el = {'cost': cost, 'year': year}
        for el, num in kwargs.items():
            copier_el[el] = num
        Copier.copier_base[model] = copier_el


s = Stock()
s.add_item('printer', 20, 'p1', 100, 2009, speed=52)
s.add_item('printer', 1, 'p2', 200, 2010, speed=108)
s.add_item('scanner', 3, 's1', 200, 2001, dpi=600)
s.add_item('copier', 20, 'c1', 250, 2015, copy_speed=10)
print('All equipment: ', OfficeEquipment.office_base)
print('Printers:', Printer.printer_base)
print('Scanners:', Scanner.scanner_base)
print('Copiers:', Copier.copier_base)
