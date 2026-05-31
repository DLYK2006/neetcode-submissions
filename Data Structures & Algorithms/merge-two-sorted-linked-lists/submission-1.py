# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node=ListNode()
        curr=node
        
        l1=list1
        l2=list2

        while l1 is not None and l2 is not None:
            if(l1.val<=l2.val):
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next

        if(l1 is None):
            while l2 is not None:
                curr.next=l2
                l2=l2.next
                curr=curr.next
        elif(l2 is None):
            while l1 is not None:
                curr.next=l1
                l1=l1.next
                curr=curr.next
        return node.next
