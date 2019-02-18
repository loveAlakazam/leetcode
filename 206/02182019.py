# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: 'ListNode') -> 'ListNode':
        if head==None or head.next==None:
            return head
        prev= None
        now= head
        after=head.next
        while after !=None:
            tmp=after.next
            after.next=now
            prev=now
            now=after
            after=tmp
        
        head.next=None
        head=now
        return head
