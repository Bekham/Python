start_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
new_word = ''
text = ''
print(start_list)
for word in start_list:  # раскладываем исходный список на строки
    find_num = 0
    for element in word:  # разбиваем каждую строку на элементы и сравниваем их с цифрами из списка num_list
        digit = element.isdigit()
        if digit:
            find_num += 1  # если есть сходство - считаем количество цифр в строке
    if find_num == 1 and len(word) == find_num:  # дополняем нулем числа до двух целочисленных разрядов
        new_word = '0' + word[:]
    elif find_num == 1 and len(word) > find_num:  # дополняем нулем числа со знаком до двух целочисленных разрядов
        new_word = word[:1] + '0' + word[1:]
    elif find_num > 1:
        new_word = word
    if find_num > 0:  # добавляем кавычки перед числами
        new_list.append('"')
        new_list.append(new_word)
        new_list.append('"')
    else:
        new_word = word
        new_list.append(new_word)
print(new_list)
for i in range(len(new_list)):  # формируем итоговую строку
    if i+2 < len(new_list) and new_list[i] == '"' and new_list[i+1][-1:].isdigit():
        text += new_list[i]
    elif new_list[i][-1:].isdigit():
        text += new_list[i]
    else:
        text += new_list[i] + ' '
print('Итог:', text)
