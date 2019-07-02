"""
将文件夹下的txt文件更改csv文件，通过改后缀的方式
"""
from pathlib import Path

DIRECTOR = 'csvs'


def unify_ext_with_path(dir: str):
    """
    :param dir: 一个文件夹
    :return: None
    """
    for txt_file in Path(dir).glob('*.txt'):
        txt_file.rename(txt_file.with_suffix('.csv'))


"""
1.使用 Path(path) 将字符串路径转换为 Path 对象
2.调用 .glob('*.txt') 对路径下所有内容进行模式匹配并以生成器方式返回，结果仍然是 Path 对象.
   所以我们可以接着做后面的操作
3.使用 .with_suffix('.csv') 直接获取使用新后缀名的文件全路径
4.调用 .rename(target) 完成重命名
"""


if __name__ == "__main__":
    unify_ext_with_path(DIRECTOR)