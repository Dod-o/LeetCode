class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        sign = 0
        if x < 0:
            x = -x
            sign = 1

        num = 0
        while x > 0:
            num = num * 10 + (x % 10)
            x = x // 10

        if sign == 1:
            num = -num

        if num < -math.pow(2, 31):
            return 0
        if num > math.pow(2, 31) - 1:
            return 0

        return num