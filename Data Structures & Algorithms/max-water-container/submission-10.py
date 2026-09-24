class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area  = 0

        while left < right: 
            # solve the area
            area  = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, area)
            
            # move the pointer that has the smaller height value to look for the best area calculation
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area

            

            