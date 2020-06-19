import math
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0: return 0

        result_neg = False
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0: result_neg = True
        dividend, divisor = math.fabs(dividend), math.fabs(divisor)

        cnt = 0
        cur_sum = 0
        cur_cnt = 0
        cur_sub_gap = dividend

        while True:
            if cur_sum == 0:
                if divisor > cur_sub_gap:
                    cnt = cnt if result_neg == False else 0-cnt
                    cnt = 2 ** 31 - 1 if cnt > 2 ** 31 - 1 else cnt
                    return cnt
                cur_sum += divisor
                cur_cnt += 1
                cur_sub_gap -= divisor
                continue
            while cur_sum + cur_sum <= cur_sub_gap:
                cur_sub_gap -= cur_sum
                cur_sum += cur_sum
                cur_cnt += cur_cnt
            cnt += cur_cnt
            cur_cnt = 0
            cur_sum = 0








        # while cur_sum < dividend:
        #     if cur_sum + cur_sum <= dividend:
        #         cur_sum += cur_sum
        #         cnt += cnt
        #     elif cur_sum + divisor <= dividend:
        #         cur_sum += divisor
        #         cnt += 1
        #     else: break
        # if result_neg == True: cnt = 0 - cnt
        # return cnt




if __name__ == '__main__':
    print(Solution().divide(10, 3))