# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        elif root2 is None:
            return root1

        def helper(root2,root1):
            if not root1:
                return root2
            if not root2:
                return root1
            
            root1.val+=root2.val
            root1.left=helper(root2.left,root1.left)
            root1.right=helper(root2.right,root1.right)
            return root1
        
        return helper(root2,root1)