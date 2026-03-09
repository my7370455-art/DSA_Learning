class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for index, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                process_height = heights[stack[-1]]
                stack.pop()
                max_area = max(max_area, process_height * (index - stack[-1] - 1 if stack else index))
            stack.append(index)

        return max_area