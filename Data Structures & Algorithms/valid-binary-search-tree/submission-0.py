# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        high = float('inf')
        low = float('-inf')
        return self.dfs(root,high,low)

    def dfs(self,root,high,low):
        if root is None:
            return True
        return low<root.val<high and self.dfs(root.left,root.val,low) and self.dfs(root.right,high,root.val)