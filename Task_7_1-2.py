import os
import yaml


def dir_maker(*args):
    dir_path = os.path.join(*args)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def dirs_finder(path_list, dirs_dict):
    if type(dirs_dict) == dict:
        for key_, item_ in dirs_dict.items():
            path_list.append(key_)
            dir_maker(*path_list)
            dirs_finder(path_list, item_)
            path_list.remove(key_)
    elif type(dirs_dict) == list:
        for item_list in dirs_dict:
            dirs_finder(path_list, item_list)
    elif dirs_dict.find('.') != -1:
        file_path = os.path.join(os.getcwd(), *path_list, dirs_dict)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(' ')
    else:
        return path_list, dirs_dict


with open('task_7_1_yaml', 'r', encoding='utf-8') as f:
    dirs = yaml.safe_load(f)
for key, item in dirs.items():
    listing = []
    if type(item) == dict:
        listing.append(key)
        dir_maker(*listing)
        dirs_finder(listing, item)
print(dirs)

