# 69. x 的平方根
# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。


from typing import *


class Solution:
    def mySqrt(self, x: int) -> int:
        return self.niudun(x)

    def niudun(self, x):
        # 根号x 就是x^2-a=0的一个正根 求导为2x则任意一点的(x,f(x))切线斜率为2x,x-f(x)/(2x)就是一个比x更接近的近似值。
        # 代入 f(x)=x^2-a得到x-(x^2-a)/(2x)，也就是(x+a/x)/2。
        if x <= 1:
            return x
        y = x
        while y > x / y:
            y = (y + x / y) // 2
        return int(y)


if __name__ == '__main__':
    test = [
        (8, 2)
    ]
    for i in test:
        print(Solution().mySqrt(i[0]) == i[1])
