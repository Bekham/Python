start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
indexes = []
text = ''
print('Номер массива: ', id(start_list))
print(start_list)
for word in start_list:
    count = 0
    for i in word:
        digit = i.isdigit()
        if digit:
            count += 1
    if count > 0:  # Запись ключей обнаруженных объектов в список списка: содержание строки, ее длинна и кол-во цифр
        indexes.append([word, len(word), count])
for num in indexes:
    if num[2] == 1 and num[1] == num[2]:  # дополняем нулем числа до двух целочисленных разрядов
        start_list.insert(start_list.index(num[0]), '0' + num[0])
        start_list.remove(num[0])
        num[0] = '0' + num[0]
    elif num[2] == 1 and num[1] > num[2]:  # дополняем нулем числа со знаком до двух целочисленных разрядов
        start_list.insert(start_list.index(num[0]), num[0][:1] + '0' + num[0][1:])
        start_list.remove(num[0])
        num[0] = num[0][:1] + '0' + num[0][1:]
    start_list.insert(start_list.index(num[0]), '"')
    start_list.insert(start_list.index(num[0]) + 1, '"')
for i in range(len(start_list)):  # формируем итоговую строку
    if i + 2 < len(start_list) and start_list[i] == '"' and start_list[i + 1][-1:].isdigit():
        text += start_list[i]
    elif start_list[i][-1:].isdigit():
        text += start_list[i]
    else:
        text += start_list[i] + ' '
print('-' * 100)
print('Номер массива: ', id(start_list))
print(start_list)
print('Итог: ', text)
