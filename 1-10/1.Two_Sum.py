class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sort_nums = sorted(nums)
        left, right = 0, len(sort_nums) - 1
        # while sort_nums[right] > target: right -= 1
        while left < right:
            num_sum = sort_nums[left] + sort_nums[right]
            if num_sum > target: right -= 1
            elif num_sum < target: left += 1
            elif num_sum == target:
                if sort_nums[left] == sort_nums[right]:
                    index1 = nums.index(sort_nums[left])
                    del nums[index1]
                    index2 = nums.index(sort_nums[right]) + 1
                    return [index1, index2]
                else:
                    return [nums.index(sort_nums[left]), nums.index(sort_nums[right])]

if __name__ == '__main__':
    # nums = [2, 7, 11, 15]
    nums = [3, 2, 4]
    target = 6

    s = Solution()
    result = s.twoSum(nums, target)
    print(result)



