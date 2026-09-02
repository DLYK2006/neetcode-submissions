
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        dummy1=ListNode()
        head.next=dummy1
        
        while list1 is not None and list2 is not None:
            if list1.val<=list2.val:
                dummy1.next=list1
                list1=list1.next
            elif list1.val>list2.val:
                dummy1.next=list2
                list2=list2.next
            dummy1=dummy1.next
            print(dummy1.val)
        
        if list1 is not None:
            dummy1.next=list1
        
        if list2 is not None:
            dummy1.next=list2

        return head.next.next