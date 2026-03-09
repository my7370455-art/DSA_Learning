class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        root_index_in_inorder = inorder.index(root_val)
        
        left_size = root_index_in_inorder
        right_size = len(preorder) - left_size - 1

        root.left = self.buildTree(preorder[1:left_size + 1], inorder[:left_size])
        root.right = self.buildTree(preorder[left_size + 1:], inorder[left_size + 1:])

        return root