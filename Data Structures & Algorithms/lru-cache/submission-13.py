class Node:
    def __init__(self, key=0,value=0):
        self.next=None
        self.key=key
        self.val=value
        self.prev=None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.most=Node()
        self.least=Node()
        self.least.next=self.most
        self.most.prev=self.least

    def get(self, key: int) -> int:
        if key in self.cache:
            temp=self.cache[key]
            self.remove(temp)
            self.add(temp)
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node=Node(key,value)
            self.cache[key]=node
            self.add(node)
        else:
            self.cache[key].val=value
            self.remove(self.cache[key])
            self.add(self.cache[key])
        
        if len(self.cache)>self.capacity:
            temp=self.least.next
            self.remove(temp)
            del self.cache[temp.key]

    def remove(self,node):
        right=node.next
        left=node.prev
        right.prev=left
        left.next=right

    def add(self,node):
        left=self.most.prev
        node.prev=left
        node.next=self.most
        self.most.prev=node
        left.next=node