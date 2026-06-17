# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        return self.dfs(root)

    def dfs(self,root):
        
        if root is None:
            return None
        print(root.val)
        if p.val<=root.val and q.val>=root.val:
            print(123)
            return root
        elif p.val>=root.val and q.val<=root.val:
            return root
        elif p.val<=root.val and q.val<=root.val:
            return self.dfs(root.left)
        else:
            return self.dfs(root.right)
        
        