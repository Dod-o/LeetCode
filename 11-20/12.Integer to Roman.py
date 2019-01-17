class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        thousand = ['M', 'MM', 'MMM']
        hundred = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        ten = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        units = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

        romanStr = ''
        n = num // 1000
        num = num % 1000
        if n != 0:romanStr += thousand[n - 1]

        n = num // 100
        num = num % 100
        if n != 0:romanStr += hundred[n - 1]

        n = num // 10
        num = num % 10
        if n != 0:romanStr += ten[n - 1]

        n = num
        if n != 0:romanStr += units[n - 1]

        return romanStr