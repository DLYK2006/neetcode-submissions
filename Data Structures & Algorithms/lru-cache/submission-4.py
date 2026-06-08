class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.stuff={}
        self.LRU=Node(0,0)
        self.MRU=Node(0,0)
        self.LRU.next=self.MRU
        self.MRU.prev=self.LRU

    def get(self, key: int) -> int:
        if(key in self.stuff):
            self.remove(self.stuff[key])
            self.insert(self.stuff[key])
            return self.stuff[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if(key not in self.stuff):
            node=Node(key,value)
            self.stuff[key]=node
            self.insert(node)

            if(len(self.stuff)>self.capacity):
                save=self.LRU.next
                self.remove(save)
                del self.stuff[save.key]

      
        elif(key in self.stuff):
            self.stuff[key].val=value
            self.remove(self.stuff[key])
            self.insert(self.stuff[key])

    def remove(self, node) -> None:
        node.prev.next=node.next
        node.next.prev=node.prev
    
    def insert(self, node)-> None:
        node.next=self.MRU
        self.MRU.prev.next=node
        node.prev=self.MRU.prev
        self.MRU.prev=node
