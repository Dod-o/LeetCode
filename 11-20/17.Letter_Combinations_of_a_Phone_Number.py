class Solution(object):
    def __init__(self):
        self.dict = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }

    def get_string(self, num_str):
        if len(num_str) == 0: return [""]
        if len(num_str) == 1: return self.dict[num_str[0]]

        final_result = []
        cur_str_cand = self.dict[num_str[0]]
        for i in range(len(cur_str_cand)):
            result = self.get_string(num_str[1:])
            for j in range(len(result)):
                final_result.append(cur_str_cand[i] + result[j])
        return final_result

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return []

        return self.get_string(digits)





if __name__ == '__main__':
    s = Solution()
    result = s.letterCombinations("23")
    print(result)