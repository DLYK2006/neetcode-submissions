# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        else:
            return self.sameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
    def sameTree(self,root1,root2):

        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None:
            return False
        return root1.val==root2.val and self.sameTree(root1.left,root2.left) and self.sameTree(root1.right,root2.right)

    