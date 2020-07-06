# 121. 买卖股票的最佳时机
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
#
# 注意：你不能在买入股票前卖出股票。


from typing import *


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 当前位置的正方形边长为 当该位置为1时 上方 左方 左上方 最小边长+1
        dp = [[0] * len(matrix[row]) for row in range(len(matrix))]
        v = 0
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == '1':
                    dp[row][column] = 1 + min([dp[row - 1][column], dp[row][column - 1], dp[row - 1][column - 1]])
                    v = max(dp[row][column], v)
                else:
                    dp[row][column] = 0
        return v * v


if __name__ == '__main__':
    test = [
        ("""1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0""", 4),
    ]
    for i in test:
        print(Solution().maximalSquare([i.split() for i in i[0].split("\n")]) == i[1])
