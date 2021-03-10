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

x = Solution()
height1 = [1,8,6,2,5,4,8,3,7]
height2 = [1, 1]
height3 = [4,3,2,1,4]
print(x.maxArea(height1))