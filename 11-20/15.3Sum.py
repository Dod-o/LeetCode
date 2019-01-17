class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        numsSorted = sorted(nums)
        returnArr = []
        if len(nums) < 3:return returnArr
        if len(nums) == 3:
            if sum(nums) == 0:
                returnArr.append([nums[0], nums[1], nums[2]])
            return returnArr

        for i in range(len(numsSorted) - 2):
            if i > 0 and numsSorted[i] == numsSorted[i - 1]:continue
            if numsSorted[i] > 0:
                break
            l = i + 1
            r = len(numsSorted) - 1
            while l < r:
                if numsSorted[i] + numsSorted[l] + numsSorted[r] < 0:
                    l += 1
                elif numsSorted[i] + numsSorted[l] + numsSorted[r] > 0:
                    r -= 1
                elif numsSorted[i] + numsSorted[l] + numsSorted[r] == 0:
                    returnArr.append([numsSorted[i], numsSorted[l], numsSorted[r]])
                    l += 1
                    r -= 1
                    while l < r and numsSorted[l] == numsSorted[l - 1]:l += 1
                    while l < r and numsSorted[r] == numsSorted[r + 1]: r -= 1
        return returnArr