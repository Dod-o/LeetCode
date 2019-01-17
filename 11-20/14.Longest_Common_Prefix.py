class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''

        minLength = len(strs[0])
        for i in range(len(strs)):
            if len(strs[i]) < minLength:
                minLength = len(strs[i])

        point = 0
        returnStr = ''

        for i in range(minLength):
            s = strs[0][i]
            flag = True
            for j in range(1, len(strs)):
                if strs[j][i] != s:
                    flag = False
            if flag == True:
                returnStr += s
            else:
                return returnStr
        return returnStr