import os
import shutil

root_dir = os.getcwd()
for root, dirs, files in os.walk(root_dir):
    if root.endswith('templates'):
        file_path = os.path.join(os.getcwd(), root.split('\\')[-3], root.split('\\')[-1], root.split('\\')[-2])
        try:
            shutil.copytree(root, file_path)
        except FileExistsError as e:
            print(e)
