class Node:
    def __init__(self,key=0,val=0 ):
        self.next=None
        self.prev=None
        self.val=val
        self.key=key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.stuff={}
        self.left=Node()
        self.right=Node()
        self.left.next=self.right
        self.right.prev=self.left

    def get(self, key: int) -> int:
        if key in self.stuff:
            node=self.stuff[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.stuff:    
            node=Node(key,value)
            self.stuff[key]=node
        else:
            self.stuff[key].val=value
            node=self.stuff[key]
            self.remove(node)
        self.insert(node)
        if len(self.stuff)>self.capacity:
            node=self.left.next
            self.remove(node)
            del self.stuff[node.key]
    

    def insert(self,node):
        prev=self.right.prev
        node.next=self.right
        node.prev=prev
        prev.next=node
        self.right.prev=node
    
    def remove(self,node):
        prev=node.prev
        prev.next=node.next
        node.next.prev=prev

        
        
        
        
        
