# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        another=dummy
        curr=head
        added=0
        while curr:
            if curr.val==0:
                dummy.val+=added
                added=0
                if curr.next is None:
                    break
                dummy.next=ListNode(0)
                dummy=dummy.next
                curr=curr.next
            else:
                added+=curr.val
                curr=curr.next
            
        return another.next
                