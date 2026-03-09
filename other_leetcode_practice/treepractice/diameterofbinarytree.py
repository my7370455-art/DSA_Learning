# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def helper(root):
            nonlocal max_diameter
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            left_longest = helper(root.left)
            right_longest = helper(root.right)
            max_diameter = max(max_diameter, left_longest + right_longest)
            return max(left_longest, right_longest) + 1
        helper(root)
        return max_diameter
        