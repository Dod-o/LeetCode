class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = sorted(nums)
        i = 0
        j = len(n) - 1
        while i < j:
            sum = n[i] + n[j]
            if sum > target:
                j -= 1
                while i < j and n[j] == n[j + 1]: j -= 1
            elif sum < target:
                i += 1
                while i < j and n[i] == n[i - 1]: i += 1
            elif sum == target:
                if n[i] == n[j]:
                    n1 = nums.index(n[i])
                    del nums[n1]
                    n2 = nums.index(n[j]) + 1
                else:
                    n1 = nums.index(n[i])
                    n2 = nums.index(n[j])
                return [n1, n2]


# test
s = Solution()
print(s.twoSum([3, 3], 6))