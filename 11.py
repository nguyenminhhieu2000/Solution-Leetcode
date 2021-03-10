class Solution:
    def maxArea(self, height):
        right = len(height)-1
        left = 0
        maxArea = 0
        while left < right:
            if height[left] > height[right]:
                area = (height[right])*(right - left)
                maxArea = max(area, maxArea)
                right -= 1
            else:
                area = (height[left])*(right - left)
                maxArea = max(area, maxArea)
                left += 1
        return maxArea
