# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        queue=deque()

        if root is None:
            return result
        
        queue.append(root)

        while queue:
            highest=-float('inf')
            for _ in range(len(queue)):
                node=queue.popleft()
                highest=max(node.val,highest)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(highest)
        
        return (result)

