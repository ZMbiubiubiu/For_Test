"""
买卖股票的最佳时机 II
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

"""


class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        # 只要后一天比当前的股票价格高，我就买入，然后后一天卖出
        # 赚到了所有交易日的钱，所有亏钱的交易日都未交易，理所当然会利益最大化
        bonus = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                bonus += prices[i + 1] - prices[i]
        return bonus
