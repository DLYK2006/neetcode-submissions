# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        hashmap=defaultdict(int)
        for i in range(len(inorder)): 
            hashmap[inorder[i]]=i
        
        def helper(in_left,in_right,post_left,post_right):

            if in_left>in_right:
                return None
            
            root_val=postorder[post_right]
            root=TreeNode(root_val)
            idx=hashmap[root_val]
            leftside=idx-in_left

            root.left=helper(in_left,idx-1,post_left,post_left+leftside-1)
            root.right=helper(idx+1,in_right,post_left+leftside,post_right-1)
            return root
        
        return helper(0,len(inorder)-1,0,len(postorder)-1)