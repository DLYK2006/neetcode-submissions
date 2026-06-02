# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head.next

        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        
        second=slow.next
        slow.next=None
        curr=second
        prev=None
        while curr is not None:
            stupid=curr.next
            curr.next=prev
            prev=curr
            curr=stupid

        while prev is not None:
            headn=head.next
            prevn=prev.next
            head.next=prev
            prev.next=headn
            print(head.val)
            print(prev.val)
            head=headn
            prev=prevn
