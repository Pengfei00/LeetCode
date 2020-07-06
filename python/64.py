# 63. 最小路径和
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。

from typing import *


class Solution:

    def minPathSum(self, obstacleGrid: List[List[int]]) -> int:
        return self.dp(obstacleGrid)

    def dp(self, obstacleGrid):
        """
        动态规划
        dp[i][j]的最小值为dp[i-1][j] 或 dp[i][j-1] +自己的最小值
        :param obstacleGrid:
        :return:
        """
        row, column = len(obstacleGrid), len(obstacleGrid[0])
        # 只与 dp[i-1][j] dp[i][j-1] 相关可以使用一维数组直接覆盖
        dp = [0] * column
        # 初始化第一列
        for i in range(column):
            if i > 0:
                dp[i] = dp[i - 1] + obstacleGrid[0][i]
            else:
                dp[i] = obstacleGrid[0][i]

        # 0,0初始化为1
        for i in range(1, row):
            for j in range(column):
                # 当前格为障碍物则设为0
                # 当前格子值
                value = obstacleGrid[i][j]
                if j > 0:
                    # 当前最小状态
                    dp[j] = min(dp[j] + value, dp[j - 1] + value)
                else:
                    dp[j] = dp[j] + value
        return dp[-1]


if __name__ == '__main__':
    print(Solution().minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))
