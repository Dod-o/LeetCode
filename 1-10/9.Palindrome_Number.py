class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        if x == 0: return True

        ori_num = x
        pali_num = 0
        while x != 0:
            pali_num = pali_num * 10 + x % 10
            x //= 10
        if ori_num == pali_num: return True
        return False


if __name__ == '__main__':
    s = Solution()
    result = s.isPalindrome(121)
    print(result)