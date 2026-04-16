# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder, postorder):
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        
        # Base case
        if len(preorder) == 1:
            return root
        
        # Find left subtree root in postorder
        left_root = preorder[1]
        left_size = postorder.index(left_root) + 1
        
        # Build subtrees
        root.left = self.constructFromPrePost(
            preorder[1:1 + left_size],
            postorder[:left_size]
        )
        
        root.right = self.constructFromPrePost(
            preorder[1 + left_size:],
            postorder[left_size:-1]
        )
        
        return root