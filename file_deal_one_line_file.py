"""
文件只有一行，使用read分块读的方法
"""

ONE_LINE_FILE = 'one_line_file.txt'


def count_w_v1(file: str) -> int:
    """
    :param file: 文件名
    :return: 'w'字符的总数
    """
    count = 0
    read_block = 10
    with open(file, 'r') as f:
        while 1:
            chunk = f.read(read_block)
            if not chunk:  # 读取完毕(当没有内容可读取时，.read返回空字符串'')
                return count
            count += chunk.count('w')
    return count


if __name__ == "__main__":
    print(count_w_v1(ONE_LINE_FILE))
