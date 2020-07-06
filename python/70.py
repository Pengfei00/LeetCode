# 70. 爬楼梯
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。


from typing import *
from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        return self.dp(n)

    def dp(self, n):
        """
        大于2层阶梯可爬方式等于前两次可爬层数相加
        :param n:
        :return:
        """
        @lru_cache(maxsize=500)
        def _(n):
            return _(n - 1) + _(n - 2) if n > 2 else n

        return _(n)

    def dirdai(self, n):
        if n == 0:
            self.num += 1
            return
        self.dirdai(n - 1)
        if n >= 2:
            self.dirdai(n - 2)


if __name__ == '__main__':
    test = [
        (3, 3),
        (2, 2)
    ]
    for i in test:
        print(Solution().climbStairs(i[0]) == i[1])
