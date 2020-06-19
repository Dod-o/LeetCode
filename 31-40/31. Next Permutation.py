# 这不是我的code...  思路错了  累坏了 不想写了
class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)
        if n<2: return nums
        i = n-1
        while i>0 and nums[i-1]>=nums[i]:
            i -= 1
        if i==0 and nums[i]==max(nums):
            return nums.reverse()
        else:
            j = n-1
            while j>i-1 and nums[j]<=nums[i-1]:
                j -= 1
            temp = nums[i-1]
            nums[i-1] = nums[j]
            nums[j] = temp
            re = nums[i:]
            for h in range (len(re)):
                nums[n-1-h] = re[h]
            return nums