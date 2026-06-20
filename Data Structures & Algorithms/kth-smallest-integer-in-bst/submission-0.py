# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count=0
    result=0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs(root,k)
        return self.result

    def dfs(self,root,k):
        if root is None:
            return None
        self.dfs(root.left,k)
        self.count+=1
        if self.count==k:
            self.result=root.val
        self.dfs(root.right,k)
        
        