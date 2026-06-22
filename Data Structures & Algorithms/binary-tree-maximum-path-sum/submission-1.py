# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum=float('-inf')
        self.dfs(root)
        return self.maximum


    def dfs(self,root):
        if root is None:
            return 0
        leftGain=max(0,self.dfs(root.left))
        rightGain=max(0,self.dfs(root.right))
        self.maximum=max(root.val+leftGain+rightGain,self.maximum)
        return root.val+max(leftGain,rightGain)