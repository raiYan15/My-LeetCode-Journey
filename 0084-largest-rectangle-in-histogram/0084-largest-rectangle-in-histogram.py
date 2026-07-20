class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        heights.append(0)
        for right in range(len(heights)):
            while stack and heights[stack[-1]] > heights[right]:
                h = heights[stack.pop()] 
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                width = right - left - 1
                area = h * width

                ans = max(ans, area) 
            stack.append(right)
        return ans                      
        