class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        maxArea = 0
        while l < r:
            Area = min(height[r], height[l]) * (r - l)
            maxArea = max(maxArea, Area)
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return maxArea