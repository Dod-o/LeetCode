class Solution:
    def divide(self, dividend: 'int', divisor: 'int') -> 'int':
        negitive = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor == 0: return 0

        result = 0
        while dividend >= divisor:
            sub = divisor
            add_num = 1
            while dividend >= (sub + sub):
                sub += sub
                add_num += add_num
            dividend -= sub
            result += add_num

        if negitive:
            result = -result

        return min(result, 2**31 - 1)


if __name__ == '__main__':
    s = Solution()
    result = s.divide(10, 3)
    print(result)

