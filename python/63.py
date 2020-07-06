# 63. 不同路径 II
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

from typing import *


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.dp(obstacleGrid)

    def then(self, obstacleGrid):
        """
        递归
        :param obstacleGrid:
        :return:
        """
        row, column = len(obstacleGrid), len(obstacleGrid[0])
        # 起点结尾为障碍物直接返回
        if obstacleGrid[0][0] == 1 or obstacleGrid[row - 1][column - 1] == 1:
            return 0
        self.res = 0
        position2V = lambda xy: obstacleGrid[xy[1]][xy[0]]
        end_position = (column - 1, row - 1)

        def _(current_position):
            if current_position == end_position:
                self.res += 1
            elif position2V(current_position) == 1:
                return
            if current_position[0] + 1 <= end_position[0]:
                _((current_position[0] + 1, current_position[1]))
            if current_position[1] + 1 <= end_position[1]:
                _((current_position[0], current_position[1] + 1))

        _((0, 0))
        return self.res

    def dp(self, obstacleGrid):
        """
        动态规划
        dp[i][j]的状态为dp[i-1][j] dp[i][j-1] 相加 （向左走的路数+向下走的路数
        :param obstacleGrid:
        :return:
        """
        row, column = len(obstacleGrid), len(obstacleGrid[0])
        # 起点结尾为障碍物直接返回
        if obstacleGrid[0][0] == 1 or obstacleGrid[row - 1][column - 1] == 1:
            return 0
        # 只与 dp[i-1][j] dp[i][j-1] 相关可以使用一维数组直接覆盖
        # 初始化第一列
        dp = [0] * column
        for i in range(column):
            if obstacleGrid[0][i] == 1:
                dp[i] = 0
            elif i > 0:
                dp[i] = dp[i - 1]
            else:
                dp[i] = 1

        # 0,0初始化为1
        for i in range(1, row):
            for j in range(column):
                # 当前格为障碍物则设为0
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                # 列数大于0 为 上+左 的数
                elif j > 0:
                    dp[j] = dp[j] + dp[j - 1]
                #  第0列 为上一列的数
                else:
                    dp[j] = dp[j]
        return dp[-1]


if __name__ == '__main__':
    print(Solution().then([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))
