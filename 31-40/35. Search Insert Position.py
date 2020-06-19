class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0: return 0
        if target < nums[0]: return 0
        if target > nums[-1]: return len(nums)

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target: left = mid + 1
            elif nums[mid] > target: right = mid - 1
            else: return mid

        if nums[left] == target: return left
        if nums[left] < target: return left + 1
        if nums[left] > target: return left


if __name__ == '__main__':
    print(Solution().searchInsert([1,3,5,6], 0))