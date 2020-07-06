# 67.二进制求和
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
#
# 输入为 非空 字符串且只包含数字 1 和 0。


from typing import *


class Solution:
    # 补0 遍历 求和
    def addBinary(self, a: str, b: str) -> str:
        alen, blen = len(a), len(b)
        maxlen = max(alen, blen)
        a, b = a.zfill(maxlen), b.zfill(maxlen)
        tmp = 0
        res = []
        for i in range(maxlen):
            v = int(a[-1 - i]) + int(b[-1 - i]) + tmp
            tmp = 0
            if v > 1:
                tmp = 1
                v = v - 2
            res.insert(0, str(v))
        if tmp:
            res.insert(0, str(tmp))
        return ''.join(res)


if __name__ == '__main__':
    test = [
        {"a": "11", "b": "1", "res": "100"},
        {"a": "1010", "b": "1011", "res": "10101"},
    ]
    for i in test:
        print(Solution().addBinary(i['a'], i['b']) == i['res'])
