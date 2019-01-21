__author__ = 'Фещук Олег Анатольевич'

import os, sys, shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def create_folder(q):
    dir_path = os.path.join(os.getcwd(), '{}'.format(q))
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')

#for i in range(1,10):
#    create_folder('dir_{}'.format(i))

def delete_folder(folder_name):
    os.rmdir(folder_name)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_folders_here():
    for i in os.listdir(os.path.join(os.getcwd())):
        if '.' not in i:
            print(i)
    return ' '

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_current_file():
    origin_file = sys.argv[0]
    shutil.copy(sys.argv[0], origin_file + '-copy.py')