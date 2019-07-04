import random

"""
需求，扫雷游戏。480个格子，需要设置100个累。从1到480每个数字代表一个格子。
"""


def set_mine(total: int, total_mines: int) -> set:
    """
    :param total: 总数
    :param total_mines: 从总数为total中随机抽取mins个
    :return:
    """
    mines = set()
    for i in range(total_mines):
        j = random.randint(1, total)
        while j in mines:
                j = random.randint(1, total)
        mines.add(j)
    return mines


if __name__ == "__main__":
    print(set_mine(480, 100))