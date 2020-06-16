class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return x

        neg = False
        if x < 0:
            neg = True
            x = -x

        result = 0
        while x != 0:
            x_remain = x % 10
            result = result * 10 + x_remain
            x = x // 10

        if neg == True: result = -result

        if result < -(2**31) or result > 2**31 - 1: return 0

        return result






if __name__ == '__main__':
    s = Solution()
    result = s.reverse(120)
    print(result)