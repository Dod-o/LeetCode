class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import math
        if len(str) == 0:
            return 0

        point = 0
        while str[point] == ' ':
            point += 1
            if point >= len(str):
                return 0
        strList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']
        if str[point] not in strList:
            return 0

        sign = 0  # 0为正数  1为负数
        if str[point] == '+':
            point += 1
        elif str[point] == '-':
            point += 1
            sign = 1
        if point == len(str):
            return 0
        num = 0
        while (ord(str[point]) >= 48) and (ord(str[point]) <= 57):
            num = num * 10 + (ord(str[point]) - 48)
            point += 1
            if point == len(str):
                break

        if sign == 1:
            num = -num
        if num < -math.pow(2, 31):
            num = -math.pow(2, 31)
        if num > math.pow(2, 31) - 1:
            num = math.pow(2, 31) - 1

        return int(num)