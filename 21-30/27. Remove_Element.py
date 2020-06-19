class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # if len(nums) == 0: return 0


        point = 0
        for i in range(len(nums)):
            if nums[i] == val: continue
            nums[point] = nums[i]
            point += 1
        return point



if __name__ == '__main__':
    print(Solution().removeElement([], 3))