# this code is worong!!!

class Solution(object):
    def match(self, s, p):
        pass

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pure_falg = True
        for i in range(len(p)):
            if p[i] in ['.','*']: pure_falg = False
        if pure_falg == True:
            if pure_falg == s: return True
            return False


        if len(s) == 0 or len(p) == 0: return False

        if len(p) == 1:
            if s[0] == p[0] or p[0] == '.': return True
            return False
        if len(p) > 1:
            if p[1] != '*':
                if s[0] == p[0] or p[0] == '.':
                    return self.isMatch(s[1:], p[1:])
                else:
                    return False
            else:
                if s[0] != p[0] and p[0] != '.':
                    if len(p) == 2: return True
                    else:
                        return self.isMatch(s, p[2:])
                elif p[0] == '.':
                    if len(p) == 2: return True
                    for i in range(len(s)):
                        result = self.isMatch(s[i:], p[2:])
                        if result == True: return True
                    return False
                elif s[0] == p[0]:
                    if len(p) == 2: return True
                    left, right = 0,0
                    for i in range(1, len(s)):
                        if s[i] == s[0]:
                            right = i
                            continue
                        else:
                            break
                    if right == len(s) - 1: return True

                    for i in range(left, right + 2):
                        result = self.isMatch(s[i:], p[2:])
                        if result == True: return True
                    return False


if __name__ == '__main__':
    s = Solution()
    result = s.isMatch("issippi", "is*p*.")
    print(result)