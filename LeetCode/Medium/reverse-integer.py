class Solution:
    def reverse(self, x: int) -> int:
        re = 0
        if x < 0: re =  - 1 * int(str(x)[::-1][:-1])
        else: re =  int(str(x)[::-1])

        if re <= -2 ** 31 or re >= 2 ** 31: return 0
        return re
