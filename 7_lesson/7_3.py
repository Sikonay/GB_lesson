import os, shutil

for root, dirs, files in os.walk('my_project'):
    #print(root,dirs,files)
    if root == r'my_project\templates':
        break
    for file in files:
        #print(file.rsplit('.', 1)[-1].lower())
        if file.rsplit('.', 1)[-1].lower() == 'html':
            print()
            os.makedirs(os.path.join(r'my_project\templates',root.split('\\')[-1]), exist_ok=True)
            shutil.copyfile(os.path.join(root,file), os.path.join(r'my_project\templates',os.path.join(root.split('\\')[-1],file)))