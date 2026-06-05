"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        crazy={}
        crazy[None] = None
        curr=head

        while curr is not None:
            crazy[curr]=Node(curr.val)
            curr=curr.next

        curr=head

        while curr is not None:
            crazy[curr].next=crazy[curr.next]
            crazy[curr].random=crazy[curr.random]
            curr=curr.next

        return crazy[head]