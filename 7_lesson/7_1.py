import os

folders = ['my_project', 'my_project/settings', 'my_project/mainapp', 'my_project/adminapp', 'my_project/authapp']

for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)

# folders = ['my_project', ['settings', 'mainapp', 'adminapp', 'authapp']]

# def recurs_folders(folder_list):
#     temp = []
#     recur = ''
#     for item in folder_list:
#         if isinstance(item, str):
#             # print(item)
#             if not os.path.isdir(item):
#                 # папки нет надо ее создать
#                 os.mkdir(item)
#                 # сохраняем
#                 recur = item
#             else:
#                 # папка есть необходимо переитти к нему
#                 os.chdir(item)
#         else:
#             # print(type(item))
#
#             os.chdir(recur)
#             recurs_folders(item)
#     return temp
#
#
# recurs_folders(folders)
