#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'colddew'

import os
import shutil


def make_succulent_train_folder(root_path):

    # for root, dirs, files in os.walk(root_path):
    #     # print(root)  # 当前目录路径
    #     # print(dirs)  # 当前路径下所有子目录
    #     # print(files)  # 当前路径下所有非目录子文件
    #     for f in files:
    #         if os.path.splitext(f)[1] == '.jpg':
    #             print(os.path.join(root, f))

    # 只处理当前文件夹根目录下的图片
    if(os.path.exists(root_path)):
        files = os.listdir(root_path)
        for f in files:
            old_path = os.path.join(root_path, f)
            print old_path
            if (os.path.isfile(old_path) and os.path.splitext(old_path)[1] == '.jpg'):
                folder = os.path.split(old_path)[1].split('-')[0]
                sub_path = mkDir(root_path, folder)
                new_path = os.path.join(sub_path, f)
                shutil.move(old_path, new_path)


def mkDir(root_path, folder):
    dir_path = root_path + folder
    exists = os.path.exists(dir_path)
    if not exists:
        os.makedirs(dir_path)
        return dir_path
    else:
        return dir_path


def rename_all_succulent_train_file(root_path):
    n = 0
    for parent, dirnames, filenames in os.walk(root_path):
        for dirname in dirnames:
            # print "parent is: " + parent
            # print "dirname is: " + dirname
            # n += 1
            # print n
            rename_current_path_succulent_train_file(os.path.join(parent, dirname))


def rename_current_path_succulent_train_file(current_path):
    n = 0
    for parent, dirnames, filenames in os.walk(current_path):
        for filename in filenames:
            if filename != '.DS_Store':
                # print "parent is: " + parent
                # print "filename is: " + filename

                old_path = os.path.join(parent, filename)
                print old_path

                n += 1
                new_file_name = os.path.split(parent)[1] + '-' + str(n) + '.jpg'
                new_path = os.path.join(parent, new_file_name)
                print new_path

                shutil.move(old_path, new_path)


# make_succulent_train_folder('/Users/anmy/Downloads/pic/succulent-train/')
# rename_all_succulent_train_file('/Users/anmy/Downloads/pic/succulent-train/')
