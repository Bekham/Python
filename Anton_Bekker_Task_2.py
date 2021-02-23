def num_translate(eng):
    translate = {'zero': 'ноль',
                 'one': 'один',
                 'two': 'два',
                 'three': 'три',
                 'four': 'четыре',
                 'five': 'пять',
                 'six': 'шесть',
                 'seven': 'семь',
                 'eight': 'восемь',
                 'nine': 'девять',
                 'ten': 'десять'
                 }
    if eng.istitle():
        return translate.get(eng.lower(), None).capitalize()
    else:
        translate.get(eng, None)


print(num_translate(input('Please, enter the number in English: ')))
