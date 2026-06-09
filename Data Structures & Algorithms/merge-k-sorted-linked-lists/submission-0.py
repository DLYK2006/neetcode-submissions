# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if(len(lists)>0):
            results=lists[0]
        else:
            return None

        for i in range(1,len(lists)):
            results=self.mergeTwoLists(results,lists[i])
        
        return results
    
    def mergeTwoLists(self,l1,l2):
        dummy=ListNode(0)
        curr=dummy
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        while l1 is not None and l2 is not None:
            if(l1.val>l2.val):
                curr.next=l2
                curr = curr.next
                l2=l2.next
            else:
                curr.next=l1
                curr = curr.next
                l1=l1.next

        if l1 is None:
            curr.next=l2
        if l2 is None:
            curr.next=l1
        
        return dummy.next
