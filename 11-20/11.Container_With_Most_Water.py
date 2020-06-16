class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1: return 0
        if len(height) == 2: return min(height)

        cur_water = min(height[0], height[-1]) * (len(height) - 1)
        left, right = 0, len(height) - 1
        max_water = cur_water

        while left < right:
            if height[left] < height[right]:
                cur_left_height = height[left]
                while left < right and height[left] <= cur_left_height:
                    left += 1
                if left >= right: break
                cur_water = min(height[left], height[right]) * (right - left)
                max_water = cur_water if cur_water > max_water else max_water
            elif height[left] > height[right]:
                cur_right_height = height[right]
                while left < right and height[right] <= cur_right_height:
                    right -= 1
                if right <= left: break
                cur_water = min(height[left], height[right]) * (right - left)
                max_water = cur_water if cur_water > max_water else max_water
            else:
                cur_tmp_left, cur_tmp_right = left, right
                while cur_tmp_left < cur_tmp_right:
                    if height[cur_tmp_left] > height[left]: break
                    if height[cur_tmp_right] > height[right]: break
                    cur_tmp_left += 1
                    cur_tmp_right -= 1
                if cur_tmp_left >= cur_tmp_right: break
                if height[cur_tmp_left] > height[left]: left = cur_tmp_left
                elif height[cur_tmp_right] > height[right]: right = cur_tmp_right
                cur_water = min((height[left], height[right])) * (right - left)
                max_water = cur_water if cur_water > max_water else max_water
        return max_water




if __name__ == '__main__':
    s = Solution()
    result = s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(result)