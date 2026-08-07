"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.graph={}
        if node is None:
            return None
        return self.dfs(node)
    
    def dfs(self,node):
        if node in self.graph:
            return self.graph[node]
        new=Node(node.val)
        self.graph[node]=new
        for neighbor in node.neighbors:
            new.neighbors.append(self.dfs(neighbor))
        return new