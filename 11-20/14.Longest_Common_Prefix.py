class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]

        point = 0
        longest_common = ""
        while True:
            if point < len(strs[0]):
                cur_char = strs[0][point]
            else: return longest_common
            all_same = True
            for i in range(1, len(strs)):
                if point < len(strs[i]) and strs[i][point] == cur_char: continue
                else:
                    all_same = False
                    break
            if all_same == True:
                longest_common += cur_char
                point += 1
            else: return longest_common






if __name__ == '__main__':
    s = Solution()
    result = s.longestCommonPrefix(["flower","flow","flight"])
    print(result)