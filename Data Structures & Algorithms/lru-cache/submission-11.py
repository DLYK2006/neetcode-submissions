class Node:
    def __init__(self,key=0,val=0):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.most=Node()
        self.least=Node()
        self.most.prev=self.least
        self.least.next=self.most
        self.grah={}

    def get(self, key: int) -> int:
        if key in self.grah:
            self.remove(self.grah[key])
            self.insert(self.grah[key])
            return self.grah[key].val
        else:
            return -1        

    def put(self, key: int, value: int) -> None:
        if key not in self.grah:
            node=Node(key,value)
            self.grah[key]=node
        else:
            node=self.grah[key]
            node.val=value
            self.remove(node)
        self.insert(node)
        if len(self.grah)>self.capacity:
            temp=self.least.next
            self.remove(temp)
            del self.grah[temp.key]

    def insert(self,node):
        prev=self.most.prev
        node.next=self.most
        self.most.prev=node
        node.prev=prev
        prev.next=node
    
    def remove(self,node):
        prev=node.prev
        prev.next=node.next
        node.next.prev=prev

