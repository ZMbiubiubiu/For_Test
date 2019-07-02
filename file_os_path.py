"""
将文件夹下的txt文件编程csv文件，通过改后缀的方式
"""
import os
import sys

DIRECTOR = 'csvs'


def unify_ext_with_os_path(dir: str):
    """
    :param dir: 一个文件夹
    :return: None
    """
    for file in os.listdir(dir):  # file{str} : '1.csv'
        basename, ext = os.path.splitext(file)  # basename{str} : '1' , ext{str} : '.csv'
        if ext == '.txt':
            os.rename(os.path.join(dir, file), os.path.join(dir, f'{basename}.csv'))


if __name__ == "__main__":
    unify_ext_with_os_path(DIRECTOR)