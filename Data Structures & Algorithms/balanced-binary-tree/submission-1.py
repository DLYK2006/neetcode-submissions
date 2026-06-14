# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    balance=True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        return self.balance

    def dfs(self,root):
        if root is None:
            return 0
        leftHeight=self.dfs(root.left)
        rightHeight=self.dfs(root.right)
        if(abs(leftHeight-rightHeight)>1):
            self.balance=False
        return 1+max(leftHeight,rightHeight)