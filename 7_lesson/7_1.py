import os

folders = ['my_project', ['settings', 'mainapp', 'adminapp', 'authapp']]
url = ''


def recurs_folders(folder_list):
    temp = []
    recur = ''
    for item in folder_list:
        if isinstance(item, str):
            # print(item)
            if not os.path.isdir(item):
                # папки нет надо ее создать и переитти к нему
                os.mkdir(item)
                recur = item
            else:
                # папка есть необходимо переитти к нему
                os.chdir(item)
        else:
            # print(type(item))
            os.chdir(recur)
            recurs_folders(item)
    return temp


recurs_folders(folders)
