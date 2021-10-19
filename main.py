import os

folder = r'C:\Temp\some_data'
# py_files = [item for item in os.listdir(folder)]
# print(py_files)
#
# py_files = [item for item in os.listdir(folder)
#             if item.lower().endswith('.py')]
#
# print(py_files)
#
# print(os.environ)
#
# py_files = [os.path.join(folder,item)
#             for item in os.listdir(folder)]
#
# print(py_files)
#
# print(os.path.exists(r'C:\Temp\some_data\ackle.bin'))
# print(os.path.exists(r'C:\Temp\some_data'))
# print(os.path.exists(r'C:\Temp\some_data\acklesdfsd.bin'))
#
# print('-----------------------------\n')
#
# print(os.path.join(r'C:\Temp\some_data','ackle.bin'))
# print(os.path.join(r'C:\Temp\some_data','acklesdfsd.bin'))

# for root, dirs, files in os.walk(folder):
#     print(root, dirs, files)

try:
    a = int('qwerty')
    print('All ok')
except:
    print('error')