"""
文件只有一行，使用read分块读的方法
利用生成器解耦函数
"""
import io
from typing import Generator

ONE_LINE_FILE = 'one_line_file.txt'


def file_reader(fp: io.TextIOBase, read_size: int = 100) -> Generator:
    """
    :param fp: 文件句柄
    :param read_size: 每次读取的文件块大小
    :return: 文件块的生成器
    """
    while 1:
        chunk = fp.read(read_size)
        if not chunk:
            break
        yield chunk


def count_w_v2(file: str) ->int:
    """
    :param file: 文件名
    :return: 'w'字符的总数
    """
    count = 0
    with open(file, 'r') as f:
        for chunk in file_reader(f):
            count += chunk.count('w')
    return count


if __name__ == "__main__":
    print(count_w_v2(ONE_LINE_FILE))
