class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        maxLetterNum = 0
        for k in range(len(s)):
            letterList = [0] * 256
            letterList[ord(s[k]) - 97] = 1
            letterNum = 1
            for i in range(k + 1, len(s)):
                if letterList[ord(s[i]) - 97] != 1:
                    letterList[ord(s[i]) - 97] = 1
                    letterNum += 1
                else:
                    break
            maxLetterNum = letterNum if letterNum > maxLetterNum else maxLetterNum
        return maxLetterNum
