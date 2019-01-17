class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ln = len(s)

        length = 0
        index = 0

        maxLength = 0
        maxIndex = 0
        for i in range(ln - 1):
            if s[i] == s[i + 1]:
                point1 = i - 1
                point2 = i + 2
                length = point2 - point1 - 1
                index = point1 + 1
                while point1 >= 0 and point2 <= ln - 1:
                    if s[point1] == s[point2]:
                        point1 -= 1
                        point2 += 1
                    else:
                        length = point2 - point1 - 1
                        index = point1 + 1
                        break
                if point1 < 0 or point2 > ln - 1:
                    length = point2 - point1 - 1
                    index = point1 + 1
                if length > maxLength:
                    maxLength = length
                    maxIndex = index
        for i in range(maxLength // 2, ln):
            point1 = i - 1
            point2 = i + 1
            length = point2 - point1 - 1
            index = point1 + 1
            while point1 >= 0 and point2 <= ln - 1:
                if s[point1] == s[point2]:
                    point1 -= 1
                    point2 += 1
                else:
                    length = point2 - point1 - 1
                    index = point1 + 1
                    break
            if point1 < 0 or point2 > ln - 1:
                length = point2 - point1 - 1
                index = point1 + 1

            if length > maxLength:
                maxLength = length
                maxIndex = index
        return s[maxIndex: maxIndex + maxLength]