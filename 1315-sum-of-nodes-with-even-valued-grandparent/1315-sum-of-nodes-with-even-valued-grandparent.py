# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, node: Optional[TreeNode]) -> int:
        def check_value(node , parent , grandparent):
            if not node:
                return 0
            ans = 0

            if grandparent and grandparent.val % 2 == 0:
                ans += node.val
            
            ans += check_value(node.left , node , parent)
            ans += check_value(node.right , node , parent)

            return ans 
        return check_value(node , None, None)        