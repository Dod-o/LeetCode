class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = [['', 0, 0, n, n]]
        ans = []
        while len(stack) != 0:
            [cur_path, l, r, remain_l, remain_r] = stack.pop()
            if remain_l == 0 and remain_r == 0:
               ans.append(cur_path)
            elif remain_l == 0:
                ans.append(cur_path + ')' * remain_r)
            elif remain_l > 0 and remain_r > 0:
                if l > r:
                    stack.append([cur_path + ')', l, r + 1, remain_l, remain_r - 1])
                stack.append([cur_path + '(', l + 1, r, remain_l - 1, remain_r])
        return ans



if __name__ == '__main__':
    s = Solution()
    result = s.generateParenthesis(3)
    print(result)