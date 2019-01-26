class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        curModifyPoint = 0
        curPoint = 1

        while curPoint < len(nums):
            if nums[curPoint - 1] == nums[curPoint]:
                curPoint += 1
            else:
                curModifyPoint += 1
                nums[curModifyPoint] = nums[curPoint]
                curPoint += 1

        for i in range(curModifyPoint + 1):
            print(nums[i])

        return curModifyPoint + 1