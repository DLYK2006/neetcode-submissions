# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        prevTail=dummy
        curr=head

        while True:
            if self.countNodes(curr) < k:
                break
            K=k
            kth=self.getk(curr,K)
            start=curr    
            new=kth.next

            prev=None
            temp=curr
            while K>0:
                ncurr=temp.next
                temp.next=prev
                prev=temp
                temp=ncurr
                K-=1

            prevTail.next=prev
            curr.next=new
            prevTail=curr
            curr=new
    
        return dummy.next

    def getk(self, curr, k):
        while curr is not None and k > 1:
            curr = curr.next
            k -= 1
        return curr
    
    def countNodes(self, curr):
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count