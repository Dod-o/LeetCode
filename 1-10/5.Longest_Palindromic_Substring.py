class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0: return ""
        if len(s) == 1: return s

        max_length = 0
        max_sub_string = ""

        i = 0
        while i < len(s) - 1:
            if i % 1 == 0.5:
                left, right = int(i - 0.5), int(i + 0.5)
            else:
                left, right = int(i), int(i)
            cnt = 0
            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                    cnt += 1
                else:
                    break

            if i % 1 == 0.5 and cnt * 2 > max_length:
                max_length = cnt * 2
                max_sub_string = s[left + 1: right]
            if i % 1 == 0 and cnt * 2 - 1 > max_length:
                max_length = cnt * 2 - 1
                max_sub_string = s[left + 1: right]

            if (len(s) - 1 - i) * 2 + 1 < max_length: return max_sub_string
            i += 0.5

        return max_sub_string






if __name__ == '__main__':
    a = ['a' for _ in range(1000)]
    s = Solution()
    result = s.longestPalindrome(a)
    print(len(result))