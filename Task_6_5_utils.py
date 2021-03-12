def name_hobby(users_path, hobby_path, name_hobby_path):
    """Объединение имен и хобби в один файл списком.
    Создание списков ФИО: Хобби в списке dict_name_hobby"""
    f_name = open(users_path, 'r', encoding='utf-8')
    f_hobby = open(hobby_path, 'r', encoding='utf-8')
    f_name_hobby = open(name_hobby_path, 'w', encoding='utf-8')
    line_name = f_name.readline()
    line_hobby = f_hobby.readline()
    dict_name_hobby = []
    while line_name or line_hobby:
        listing = []
        line_name = f_name.readline()
        line_hobby = f_hobby.readline()
        if line_name:
            listing = line_name[:line_name.find('\n')].split(',')
            listing.append(':')
        else:
            f_name.close()
            f_hobby.close()
            f_name_hobby.close()
            print(dict_name_hobby)
            exit(-1)
        if line_hobby:
            listing.append(line_hobby[:line_hobby.find('\n')])
        else:
            listing.append('None')
        f_name_hobby.write(' '.join(listing) + '\n')
        dict_name_hobby.append(listing)
    f_name.close()
    f_hobby.close()
    f_name_hobby.close()
    print(dict_name_hobby)


if __name__ == '__main__':
    name_hobby('users.csv', 'hobby.csv', 'name_hobby.txt')
