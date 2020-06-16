class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0: return 0

        str = str.strip()
        if len(str) == 0: return 0

        neg = False
        if str[0] == '+': str = str[1:]
        elif str[0] == '-':
            neg = True
            str = str[1:]

        num = 0
        for index in range(len(str)):
            if 48 <= ord(str[index]) <= 57:
                num = num * 10 + int(str[index])
            else:
                break

        if neg: num = -num

        if num < -(2**31): return -(2**31)
        if num > 2**31 - 1: return 2**31 - 1

        return num



if __name__ == '__main__':
    s = Solution()
    result = s.myAtoi("-91283472332")
    print(result)