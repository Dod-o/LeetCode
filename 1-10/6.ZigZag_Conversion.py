class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        str = ''
        for i in range(numRows):
            gap = (numRows - 3) * 2 + 4
            if i == numRows - 1:
                lineGap = gap
            else:
                lineGap = gap - i * 2
            if gap == lineGap:
                point = i
                while point < len(s):
                    str += s[point]
                    point = point + lineGap
            else:
                point = i
                while point < len(s):
                    str += s[point]
                    point = point + lineGap
                    lineGap = gap - lineGap
        return str