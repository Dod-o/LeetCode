class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        point = 0
        cur_index = 1
        while cur_index < len(nums):
            if nums[cur_index] == nums[point]:
                cur_index += 1
                continue
            point += 1
            nums[point] = nums[cur_index]
        return point + 1

if __name__ == '__main__':
    result = Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    print(result)