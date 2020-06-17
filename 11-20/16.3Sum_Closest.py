import math

class Solution(object):
    def two_sum(self, nums, target):
        left, right = 0, len(nums) - 1

        closest_gap = 2**32
        closest_nums = []
        while left < right:
            if nums[left] * 2 > target:
                cur_sum = nums[left] + nums[left + 1]
                cur_gap = math.fabs(cur_sum - target)
                if cur_gap < closest_gap:
                    return [nums[left], nums[left + 1]]
            if nums[right] * 2 < target:
                cur_sum = nums[right] + nums[right - 1]
                cur_gap = math.fabs(cur_sum - target)
                if cur_gap < closest_gap:
                    return [nums[right], nums[right - 1]]

            cur_sum = nums[left] + nums[right]
            cur_gap = math.fabs(cur_sum - target)
            if cur_gap < closest_gap:
                closest_gap = cur_gap
                closest_nums = [nums[left], nums[right]]

            if cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1
            else:
                return [nums[left], nums[right]]
        return closest_nums

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3: return None
        if len(nums) == 3: return sum(nums)
        nums = sorted(nums)

        closest_gap = 2**32
        closest_sum = 0
        for i in range(len(nums) - 2):
            if nums[i] * 3 > target:
                cur_sum = sum(nums[i: i + 3])
                cur_gap = math.fabs(cur_sum - target)
                if cur_gap < closest_gap:
                    closest_gap = cur_gap
                    closest_sum = cur_sum
                break

            cur_sum = nums[i] + sum(self.two_sum(nums[i + 1:], target - nums[i]))
            cur_gap = math.fabs(cur_sum - target)
            if cur_gap < closest_gap:
                closest_sum = cur_sum
                closest_gap = cur_gap
                if cur_gap == 0: return closest_sum
        return closest_sum



if __name__ == '__main__':
    s = Solution()
    result = s.threeSumClosest([1,2,5,10,11], 12)
    print(result)