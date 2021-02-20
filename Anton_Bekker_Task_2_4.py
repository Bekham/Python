start_list = ['инженер-конструктор Игорь',
              'главный бухгалтер МАРИНА',
              'токарь высшего разряда нИКОЛАй',
              'директор аэлита']
for words in start_list:
    name = words.split(' ')
    print(f'Привет, {name[-1].title()}!')
