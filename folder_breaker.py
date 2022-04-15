'''
フォルダからすべてのファイルを外に出してフォルダを削除するモジュール
---------------------------------------------------------------------------------------
・ファイルを出して空になったフォルダは削除されます
・ファイル移動の際に同じファイル名が存在した場合は、末尾に数値を付けて自動リネームする機能付き
---------------------------------------------------------------------------------------
引数は1つで、下記Exampleの"ParentDir"のフルパスを与える

Example:
(Before)
  ParentDir
   |-aaa.jpg
   |-bbb.jpg
   |-SubDir
   |  |-bbb.jpg
   |  |-ccc.jpg
   |-SubDir_2
      |-aaa.jpg
      |-bbb.jpg
(After)
  ParentDir
   |-aaa.jpg
   |-bbb.jpg
   |-bbb_0.jpg
   |-ccc.jpg
   |-aaa_0.jpg
   |-bbb_1.jpg
'''

'''
<History>
    2022.04.15 Version 1.0.0 Released.
'''

import os
import sys
import glob
import shutil
import datetime

def test():
    path = os.getcwd()
    path = os.path.join(path, 'test')
    breakAllFolder(path) 

# ファイル名を"***_0.jpg"のように、語尾に数値を付ける形に改名したパスを返す
def getRenamedFilePath(current_file_path):

    file_b_name = os.path.basename(current_file_path)
    spled_bname = os.path.splitext(file_b_name)
    without_ext = spled_bname[0]
    spled_num = without_ext.split("_")
    
    num = 0
    without_num = spled_num[0]
    if len(spled_num) > 1:
        num = int(spled_num[1])
        num += 1
    else:
        num = 0

    renamed_bname = without_num + '_' + str(num) + spled_bname[1]

    dir_path = os.path.dirname(current_file_path)
    renamed_path = os.path.join(dir_path, renamed_bname)

    return renamed_path

# 指定したフォルダの中身を全てparent pathに出してからフォルダを消す
def breakFolder(dir_path, parent_path):
    if os.path.isdir(dir_path):
        # Get all file names
        fil = dir_path + '/*.*'
        items = glob.glob(fil)

        # Move files
        #------------------------------------------------------------------
        n_items = len(items)
        print('Found', n_items, 'files in ' + '"' + dir_path + '".')
        for item in items:
            item_name = os.path.basename(item)
            cur_path = item
            while True:
                try:
                    shutil.move(cur_path, parent_path)
                except:
                    while True:
                        try:
                            renamed_filepath = getRenamedFilePath(cur_path)
                            os.rename(cur_path, renamed_filepath)
                            print(item, 'is renamed to', renamed_filepath)
                        except:
                            print('Rename Error.Try again...')
                            cur_path = renamed_filepath
                        break
                    continue

                break
        try:
            shutil.rmtree(dir_path)
        except:
            pass
        
        print('Completed!')

    # In case of directory is not found, display an error message.
    else:
        print('Error: Not found a path "' + dir_path + '".')
    return 0

# 指定した親ディレクトリ以下のディレクトリ内のファイルをすべて親ディレクトリへ移動して、空ディレクトリは削除する
def breakAllFolder(parent_dir_path):
    if os.path.isdir(parent_dir_path):
        d_list = []
        for curDir, dirs, files in os.walk(parent_dir_path, topdown=False):
            print('Directory Searching...')
            print(curDir)
            print(dirs)
            print(files)
            d_list.append(curDir)
        print('Found', len(d_list) ,'Directories:')
        for d_path in d_list:
            print(d_path)

        print('Move all files to the parent directory.')

        for d_path in d_list:
            if d_path == parent_dir_path:
                break
            else:
                breakFolder(d_path, parent_dir_path)

    else:
        print('Error: Not found a path "' + parent_dir_path + '".')
    return 0


if __name__ == '__main__':
    parent_dir_path = args[1]
    if os.path.isdir(parent_dir_path):
        breakAllFolder(parent_dir_path)
    else:
        print('ERROR: Directory is not found.')



