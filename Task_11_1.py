class Date:
    @classmethod
    def date(cls, param):
        try:
            date_int = [int(i) for i in param.split('-')]
            Date.validate(date_int)
        except ValueError:
            print('Wrong format!')

    @staticmethod
    def validate(date):
        if not 1 <= date[0] <= 31:
            print('Date value error!')
        elif not 1 <= date[1] <= 12:
            print('Month value error!')
        elif not 1 <= date[2] <= 2021:
            print('Year value error!')
        else:
            print('Correct date')


Date.date(input('Enter the date (Format: XX-XX-XXXX):'))
