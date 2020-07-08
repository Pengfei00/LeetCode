# 面试题 16.11. 跳水板
# 你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为shorter，长度较长的木板长度为longer。你必须正好使用k块木板。编写一个方法，生成跳水板所有可能的长度。
#
# 返回的长度需要从小到大排列。
#

from typing import *


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        # 最后的结果是个等差数列
        # 公差为长木板-短木板
        # 起始项为k块短木板 结束项为k块长木板
        # 长短相同直接返回
        # 0块木板直接返回
        if not k:
            return []
        if shorter == longer:
            return [shorter * k]
        return list(range(shorter * k, longer * k + 1, longer - shorter))


if __name__ == '__main__':
    test = [
        (1, 2, 3,4),
    ]
    for i in test:
        print(Solution().divingBoard(i[0], i[1],i[2]) == i[3])
