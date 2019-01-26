class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        curModigyPoint = 0
        curPoint = 0

        while curPoint < len(nums):
            if nums[curPoint] == val:
                curPoint += 1
            else:
                nums[curModigyPoint] = nums[curPoint]
                curModigyPoint += 1
                curPoint += 1

        return curModigyPoint