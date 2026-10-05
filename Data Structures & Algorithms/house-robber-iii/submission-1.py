# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache={}

        def helper(node):
            if node in cache:
                return cache[node]
            
            if node is None:
                return 0
            
            robbed=node.val
            if node.left:
                robbed+=helper(node.left.left)+helper(node.left.right)
            
            if node.right:
                robbed+=helper(node.right.right)+helper(node.right.left)
            
            skipped=helper(node.left)+helper(node.right)
            final=max(skipped,robbed)
            cache[node]=final
            return final
        
        return helper(root
        )



        

            