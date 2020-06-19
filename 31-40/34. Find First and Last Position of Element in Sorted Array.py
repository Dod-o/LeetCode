class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0: return [-1, -1]
        if len(nums) == 1: return [0, 0] if target == nums[0] else [-1, -1]

        left, right = 0, len(nums) - 1
        target_point = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                target_point = mid
                break
        if target_point == -1: return [-1, -1]

        target_left, target_right = target_point, target_point
        if target_point < len(nums) - 1 and nums[target_point + 1] == target:
            left = target_point + 1
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if mid < len(nums) - 1 and nums[mid + 1] == target:
                        left = mid + 1
                    else:
                        target_right = mid
                        break
                else:
                    right = mid - 1
        if target_point > 0 and nums[target_point - 1] == target:
            left = 0
            right = target_point - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if mid > 0 and nums[mid - 1] == target:
                        right = mid - 1
                    else:
                        target_left = mid
                        break
                else:
                    left = mid + 1
        return [target_left, target_right]




if __name__ == '__main__':
    print(Solution().searchRange([5,7], 9))