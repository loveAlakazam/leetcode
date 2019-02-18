# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        if head==None or head.next==None:
            return head
        
        n= head.next
        head.next= self.swapPairs(head=head.next.next)
        n.next= head
        return n
