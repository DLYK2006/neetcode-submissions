class ListNode:
    def __init__(self,key,next=None):
        self.key=key
        self.next=next

class MyHashSet:

    def __init__(self):
        self.set=[]
        for i in range(10**4):
            self.set.append(ListNode(0))

    def add(self, key: int) -> None:
        curr=self.set[key%len(self.set)]
        while curr.next:
            if curr.next.key==key:
                return
            curr=curr.next
        curr.next=ListNode(key)
        
    def remove(self, key: int) -> None:
        curr=self.set[key%len(self.set)]
        while curr is not None and curr.next is not None:
            if curr.next.key==key:
                curr.next=curr.next.next
            curr=curr.next

    def contains(self, key: int) -> bool:
        curr=self.set[key%len(self.set)]
        while curr.next:
            if curr.next.key==key:
                return True
            curr=curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)