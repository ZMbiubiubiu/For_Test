"""
高德纳置乱算法
将最后一个数和前面任意 n-1 个数中的一个数进行交换，
然后倒数第二个数和前面任意 n-2 个数中的一个数进行交换
以此类推
"""
import random


def gartner_wash(a: 'iterable', n: int) -> 'iterable':
    """

    :param a: 可迭代对象
    :param n: 从a中随机选取n个
    :return: 返回随机选取的值
    """
    a = list(a)
    for i in reversed(range(len(a))):
        j = random.randint(0, i)
        a[i], a[j] = a[j], a[i]
    return a[:n]


if __name__ == "__main__":
    print(gartner_wash(range(100), 50))