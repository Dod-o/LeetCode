class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        if len(needle) > len(haystack):
            return -1
        if len(haystack) == len(needle) and haystack != needle:
            return -1
        if haystack == needle:
            return 0


        for i in range(len(haystack)):
            p = i
            q = 0
            while (q < len(needle) and (p < len(haystack))) and haystack[p] == needle[q]:
                p += 1
                q += 1

            if q >= len(needle):
                return i

        return -1
