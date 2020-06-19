class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0: return ''
        if n == 1: return '1'

        cur_str = '1'
        new_str = ''
        for i in range(1, n):
            cur_cnt = 1
            j = 0
            while j < len(cur_str) - 1:
                if cur_str[j + 1] == cur_str[j]:
                    cur_cnt += 1
                else:
                    new_str += str(cur_cnt) + cur_str[j]
                    cur_cnt = 1
                j += 1
            new_str += str(cur_cnt) + cur_str[-1]
            cur_str = new_str
            new_str = ''
        return cur_str




if __name__ == '__main__':
    print(Solution().countAndSay(3))
    print(Solution().countAndSay(4))
    print(Solution().countAndSay(5))