# 121. 买卖股票的最佳时机
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
#
# 注意：你不能在买入股票前卖出股票。


from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 当天买当天卖相加
        res = 0
        for i in range(1, len(prices)):
            res += max(prices[i] - prices[i - 1], 0)
        return res


if __name__ == '__main__':
    test = [
        ([7, 1, 5, 3, 6, 4], 7),
        ([1, 2, 3, 4, 5], 4),
    ]
    for i in test:
        print(Solution().maxProfit(i[0]) == i[1])
