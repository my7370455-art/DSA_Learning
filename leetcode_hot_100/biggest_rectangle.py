class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        max_area = 0
        n_cols = len(matrix[0])
        heights = [0] * (n_cols + 1)  # Extra element to handle the stack at the end

        for row in matrix:
            for index, j in enumerate(row):
                if j == '1':
                    heights[index] += 1
                else:
                    heights[index] = 0

            stack = [-1]  # Initialize stack with a sentinel index
            for i in range(n_cols + 1):
                while heights[i] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)

        return max_area
