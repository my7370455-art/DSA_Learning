# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        pointer = root
        while pointer or stack:
            while pointer:
                stack.append(pointer)
                pointer = pointer.left
            left = stack.pop()
            result.append(left.val)
            pointer = left.right
        return result
