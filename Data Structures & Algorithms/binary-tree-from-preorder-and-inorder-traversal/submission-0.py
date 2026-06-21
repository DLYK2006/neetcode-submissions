# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.index=0
        self.grah={}
        for i in range(len(inorder)):
            self.grah[inorder[i]]=i
        return self.making(preorder,0,len(inorder)-1)

    def making(self,preorder,left,right):
        if left>right:
            return None
        rootVal=preorder[self.index]
        self.index+=1
        root=TreeNode(rootVal)
        mid=self.grah[rootVal]
        root.left=self.making(preorder,left,mid-1)
        root.right=self.making(preorder,mid+1,right)
        return root