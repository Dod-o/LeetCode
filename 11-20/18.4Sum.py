class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4: return []
        if len(nums) == 4:
            if sum(nums) == target: return [nums]
            return []

        nums = sorted(nums)

        final_result = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]: continue
            if sum(nums[i: i + 4]) > target: break
            if sum(nums[-4:]) < target: break

            three_target = target - nums[i]

            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]: continue
                if sum(nums[j:j + 3]) > three_target: break
                if sum(nums[-3:]) < three_target: break

                two_target = three_target - nums[j]

                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == two_target:
                        final_result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]: left += 1
                        while left < right and nums[right] == nums[right + 1]: right -= 1
                    elif nums[left] + nums[right] < two_target:
                        left += 1
                    elif nums[left] + nums[right] > two_target:
                        right -= 1
        return final_result

if __name__ == '__main__':
    s = Solution()
    result = s.fourSum([1, 0, -1, 0, -2, 2], 0)
    print(result)
