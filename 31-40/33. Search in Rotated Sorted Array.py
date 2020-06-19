class Solution(object):
    def sub_search(self, nums, left, right, target):
        if left > right: return -1
        if left == right: return left if nums[left] == target else -1

        if nums[left] <= nums[right]:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target: left = mid + 1
                elif nums[mid] > target: right = mid - 1
                else: return mid
            return -1
        else:
            if left + 1 == right:
                if target in nums[left: right + 1]:
                    return left if nums[left] == target else right
                return -1
            mid = (left + right) // 2
            if nums[mid] == target: return mid
            if nums[mid] > nums[left]:
                if nums[left] <= target < nums[mid]:
                    return self.sub_search(nums, left, mid - 1, target)
                else:
                    return self.sub_search(nums, mid + 1, right, target)
            else:
                if target < nums[mid]: return self.sub_search(nums, left, mid - 1, target)
                else:
                    if target > nums[right]:
                        return self.sub_search(nums, left, mid - 1, target)
                return self.sub_search(nums, mid + 1, right, target)


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0: return -1
        if len(nums) == 1: return 0 if nums[0] == target else -1
        if len(nums) == 2:
            if target in nums: return nums.index(target)
            return -1
        return self.sub_search(nums, 0, len(nums) - 1, target)





if __name__ == '__main__':
    print(Solution().search([5,1,2,3,4], 1))