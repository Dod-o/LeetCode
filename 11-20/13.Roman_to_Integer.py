class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        thousand = ['M', 'MM', 'MMM']
        hundred = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        ten = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        units = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

        intNum = 0
        roman = s
        for i in range(len(thousand) - 1, -1, -1):
            if roman.startswith(thousand[i]):
                intNum += 1000 * (i + 1)
                ln = len(thousand[i])
                roman = roman[ln:]
                break

        for i in range(len(hundred) - 1, -1, -1):
            if roman.startswith(hundred[i]):
                intNum += 100 * (i + 1)
                ln = len(hundred[i])
                roman = roman[ln:]
                break

        for i in range(len(ten) - 1, -1, -1):
            if roman.startswith(ten[i]):
                intNum += 10 * (i + 1)
                ln = len(ten[i])
                roman = roman[ln:]
                break

        for i in range(len(units) - 1, -1, -1):
            if roman.startswith(units[i]):
                intNum += 1 * (i + 1)
                ln = len(units[i])
                roman = roman[ln:]
                break

        return intNum