# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    number=0
    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root,-101)
        return self.number

    def dfs(self,root,grah):
        if root is None:
            return None
        maximum=max(root.val,grah)
        if(root.val>=maximum):
            self.number+=1
        print(maximum)
        print(self.number)
        self.dfs(root.left,maximum)
        self.dfs(root.right,maximum)
