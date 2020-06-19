class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0: return 0
        if len(needle) > len(haystack): return -1
        if len(needle) == len(haystack) and needle != haystack: return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1



if __name__ == '__main__':
    print(Solution().strStr("hello", "ll"))