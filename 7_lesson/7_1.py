import os

folders = ['my_project', ['settings', 'mainapp', 'adminapp', 'authapp']]


def recurs_folders(folder_list):
    temp = []
    for item in folder_list:
        if isinstance(item, str):
            print(item)
            print(type(item))
        else:
            print(recurs_folders(item))
            print(type(item))

print(recurs_folders(folders))

# for item in folders:
#     if isinstance(item,str):
#         item
#     else:
#         return


# print([item for sublist in folders for item in sublist])
# def cread_folders(*args):
#     for item in args:
#         print(item)

# cread_folders(folders)
