class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        if len(s) == 1: return 1

        repeat_word_dict = {}
        max_cnt = 0

        cur_left = 0
        cur_pos = 0
        cur_cnt = 0
        while cur_left < len(s):
            if s[cur_pos] not in repeat_word_dict.keys():
                repeat_word_dict[s[cur_pos]] = cur_pos
            else:
                if repeat_word_dict[s[cur_pos]] < cur_left:
                    repeat_word_dict[s[cur_pos]] = cur_pos
                else:
                    cur_cnt = cur_pos - cur_left
                    if cur_cnt > max_cnt: max_cnt = cur_cnt
                    cur_left = repeat_word_dict[s[cur_pos]] + 1
                    cur_cnt = cur_pos - cur_left + 1
                    repeat_word_dict[s[cur_pos]] = cur_pos
            cur_pos += 1
            if cur_pos == len(s):
                cur_cnt = cur_pos - cur_left
                if cur_cnt > max_cnt: max_cnt = cur_cnt
                return max_cnt

        if cur_left == len(s):
            if cur_cnt > max_cnt: max_cnt = cur_cnt

        return max_cnt




if __name__ == '__main__':
    s = Solution()
    result = s.lengthOfLongestSubstring("pwwkew")
    print(result)