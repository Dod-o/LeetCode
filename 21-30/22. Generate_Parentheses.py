class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        ans = []
        stack = [['', 0, 0, n, n]]
        while stack:
            path, cl, cr, l, r = stack.pop()
            if l == r == 0:
                ans.append(path)
            elif l == 0:
                ans.append(path + ')' * r)
            elif l > 0 and r > 0:
                if cl > cr:
                    stack.append([path + ')', cl, cr + 1, l , r - 1])
                stack.append([path + '(', cl + 1, cr, l - 1, r])
        return list(ans)
