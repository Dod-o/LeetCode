class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        stack = []
        for i in range(len(s)):
            if len(stack) == 0:
                if s[i] in match.keys(): return False
                stack.append(s[i])
            else:
                if s[i] in match.keys():
                    if stack[-1] == match[s[i]]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(s[i])
        if len(stack) != 0: return False
        return True




if __name__ == '__main__':
    s = Solution()
    result = s.isValid("{[]}")
    print(result)