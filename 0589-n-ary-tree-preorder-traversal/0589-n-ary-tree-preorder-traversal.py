"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def children(Node):
            if not Node:
                return 
            result.append(Node.val)
            for child in Node.children:
                children(child)
            
        
        children(root)
        return result 
        