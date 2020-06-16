class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= 0: return ""
        if numRows == 1 or numRows >= len(s): return s
        if numRows > len(s): return s


        result = ""
        for i in range(numRows):
            if (i == 0) or (i == numRows - 1):
                x = 0
                while i + (numRows + (numRows - 2)) * x < len(s):
                    result += s[(numRows + (numRows - 2)) * x + i]
                    x += 1
            else:
                x = 0
                while True:
                    if i + (numRows + (numRows - 2)) * x < len(s):
                        result += s[i + (numRows + (numRows - 2)) * x]
                    else:
                        break
                    if i + (numRows + (numRows - 2)) * (x + 1) - i * 2 < len(s):
                        result += s[i + (numRows + (numRows - 2)) * (x + 1) - i * 2]
                    x += 1
        return result



if __name__ == '__main__':
    s = Solution()
    result = s.convert("AB",1)
    print(result)