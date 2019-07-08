"""
 Pow(x, n)
 实现 pow(x, n) ，即计算 x 的 n 次幂函数。

 分治算法、递归

 x ^ n
 x * x * x * x * ... * x
 可以将其一分为二，
 如果为偶数, x ^ n = (x ^ (n/2) ) ^ 2
 如果为奇数，x ^ n = (x ^ ((n-1)/2) ) ^ 2 * x
"""


class Solution:

    # method 1.递归
    def myPow(self, x: float, n: int) -> float:
        # 递归基（有两个）
        if not n:
            return 1
        if n == 1:
            return x
        # 如果n为负数，则求倒数
        if n < 0:
            return 1 / self.myPow(x, -n)
        # 此为分治，根据n的奇偶性。
        if n % 2 == 1:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n // 2)

    #method 2.非递归
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n:
            if n & 1:  # 判断n的奇偶性
                result *= x
            x *= x
            n >>= 1
        return result

