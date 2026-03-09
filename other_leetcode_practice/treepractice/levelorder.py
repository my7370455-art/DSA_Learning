# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        queue1 = [root]
        queue2 = []
        output = []
        while queue1:
            output.append([])
            while queue1:
                process = queue1.pop(0)
                output[-1].append(process.val)
                if process.left:
                    queue2.append(process.left)
                if process.right:
                    queue2.append(process.right)
            if queue2:
                output.append([])
                while queue2:
                    process = queue2.pop(0)
                    output[-1].append(process.val)
                    if process.left:
                        queue1.append(process.left)
                    if process.right:
                        queue1.append(process.right)

        return output