class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        mono_stack = []
        left_bound = [0] * len(height)
        right_bound = [0] * len(height)
        for i, h in enumerate(height):
            if not mono_stack or h >= mono_stack[-1]:
                mono_stack.append(h)
            else:
                left_bound[i] = mono_stack[-1]
        mono_stack.clear()
        for i in range(len(height) - 1, -1, -1):
            h = height[i]
            if not mono_stack or h >= mono_stack[-1]:
                mono_stack.append(h)
            else:
                right_bound[i] = mono_stack[-1]

        res = 0
        for i in range(len(height)):
            if left_bound[i] and right_bound[i]:
                res += min(left_bound[i], right_bound[i]) - height[i]
        return res
