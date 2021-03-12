from Task_6_5_utils import name_hobby
import sys

if sys.argv[0]:
    users_path = input(r'Введите путь к файлу users.csv (Например: D:\users.csv): ')
    hobby_path = input(r'Введите путь к файлу hobby.csv (Например: D:\hobby.csv): ')
    name_hobby_path = input(r'Введите путь к объединенному файлу name_hobby.csv (Например: D:\name_hobby.txt): ')
    if users_path:
        users = users_path
    else:
        users = 'users.csv'
    if hobby_path:
        hobby = hobby_path
    else:
        hobby = 'hobby.csv'
    if name_hobby_path:
        name_hobby_ = name_hobby_path
    else:
        name_hobby_ = 'name_hobby.txt'
    name_hobby(users, hobby, name_hobby_)
