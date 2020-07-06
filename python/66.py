# 66. 加一
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。


from typing import *


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        tmp = 0
        digits[-1] = digits[-1] + 1
        for index, i in enumerate(digits[::-1], 0):
            position = -1 - index
            digits[position] = digits[position] + tmp
            tmp = digits[position] // 10
            if tmp:
                digits[position] = digits[position] % 10
            else:
                break
        else:
            if tmp:
                digits.insert(0, tmp)
        return digits


if __name__ == '__main__':
    test = [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([9, 9, 9], [1, 0, 0, 0])
    ]
    for k, v in test:
        print(Solution().plusOne(k) == v)
