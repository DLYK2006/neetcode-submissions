# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0 or lists[0] is None:
            return None
        while len(lists)>1:
            merged=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                if i+1<len(lists):
                    l2=lists[i+1]
                else:
                    l2=None
                merged.append(self.merge2(l1,l2))
            lists=merged
        
        return lists[0]

    def merge2(self,l1,l2):
        dummy=ListNode()
        curr=dummy

        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        while l1 is not None and l2 is not None:
            if l1.val<l2.val:
                curr.next=l1
                curr=curr.next
                l1=l1.next
            else:
                curr.next=l2
                curr=curr.next
                l2=l2.next
        
        if l1 is None:
            curr.next=l2

        if l2 is None:
            curr.next=l1

        return dummy.next 

    