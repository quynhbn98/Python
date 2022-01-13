# https://leetcode.com/problems/reverse-integer/

def reverse(self, x: int) -> int:
    if x >= 0:
        y = str(x)[::-1]
        z = int(y)
    else:
        y = str(-x)[::-1]
        z = -int(y)
    if z in range(-2 ** 31, 2 ** 31):
        return z
    else:
        return 0