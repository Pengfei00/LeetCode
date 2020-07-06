# 65. 有效数字
# 验证给定的字符串是否可以解释为十进制数字。

from typing import *


class Solution:
    def judge(self, s, has_e):
        has_double = False
        has_value = False
        start = 0
        if not s:
            return False
        if s[0] in ["-", "+"]:
            start = 1
        for i in s[start:]:
            if i == "e":
                if has_e:
                    return False
                else:
                    has_e = True
            elif i == ".":
                if has_double or has_e:
                    return False
                else:
                    has_double = True
            elif i in ["-", "+"]:
                return False
            elif not i.isdigit():
                return False
            elif has_value is False:
                has_value = True
        return has_value if (has_double or start == 1) else True

    def isNumber(self, s: str) -> bool:
        s = s.strip()
        v = s.split("e")
        if len(v) > 2:
            return False
        for index, i in enumerate(v):
            if self.judge(i, index > 0) is False:
                return False
        return True


if __name__ == '__main__':
    test = {"0": True, " 0.1 ": True, "abc": False, "1 a": False, "2e10": True, " -90e3 ": True, " 1e": False,
            "e3": False, " 6e-1": True, " 99e2.5 ": False, "53.5e93": True, " --6 ": False, "-+3": False,
            "95a54e53": False, ".": False, ".1": True, "-.1": True, "1.": True, "005047e+6": True, "46.e3": True,
            ".2e81": True, "+e": False, "4e+": False}
    for k, v in test.items():
        print(Solution().isNumber(k) == v)
