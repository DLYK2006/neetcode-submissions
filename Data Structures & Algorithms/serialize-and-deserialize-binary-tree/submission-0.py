# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        delimeter=','
        self.values=[]
        self.dfs1(root)
        result=delimeter.join(self.values)
        return result
        
    def dfs1(self,root):    
        if root is None:
            self.values.append("null")
            return None
        self.values.append(str(root.val))
        self.dfs1(root.left)
        self.dfs1(root.right)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        grah=data.split(',')
        self.number=0
        return self.dfs2(grah)

    def dfs2(self,grah):
        if grah[self.number]=='null':
            self.number+=1
            return None
        root=TreeNode(int(grah[self.number]))
        self.number+=1
        root.left=self.dfs2(grah)
        root.right=self.dfs2(grah)
        return root
            

        