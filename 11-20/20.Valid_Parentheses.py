class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        sighDict = {'}':'{', ']':'[', ')':'('}
        stack = []

        point = 0
        stack.append(s[point])

        for i in range(1, len(s)):
            if s[i] in sighDict.keys():
                if point >= 0 and stack[point] == sighDict[s[i]]:
                    del (stack[point])
                    point -= 1
                else:
                    return False
            else:
                stack.append(s[i])
                point += 1
        if len(stack) == 0:
            return True
        else:
            return False