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
        if not prices:
            return 0
        v = prices[0]
        res = 0
        for i in prices:
            if i < v:
                v = i
            elif i > v:
                res = max(res, i - v)
        return res


if __name__ == '__main__':
    test = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ]
    for i in test:
        print(Solution().maxProfit(i[0]) == i[1])
