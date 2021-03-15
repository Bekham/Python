import os
from json import dump

root_dir = r'c:\users\antonio\desktop\learning\venv\lib\site-packages\django'
files_result = {}
for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_path = os.path.join(root, file)
        size = os.path.getsize(file_path)
        size_round = 10 ** len(str(size))
        ext = file.rsplit('.', maxsplit=1)[-1].lower()
        if size_round in files_result.keys():
            files_result[size_round][0] += 1
            files_result[size_round][1].add(ext)
        else:
            files_result[size_round] = [1, set()]
            files_result[size_round][1].add(ext)
for i in files_result:
    files_result[i][1] = tuple(files_result[i][1])
print(files_result)
file_name = f'{os.path.split(root_dir)[-1]}_summary.json'
with open(file_name, 'w', encoding='utf-8') as f:
    dump(files_result, f, indent=4, sort_keys=True)
