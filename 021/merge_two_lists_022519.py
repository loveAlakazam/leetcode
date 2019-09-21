# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        head=None
        if l1.val<=l2.val:
            head=l1
            l1=l1.next
        else:#l1.val>l2.val
            head=l2
            l2=l2.next
        
        l=head    
        while l1 is not None and l2 is not None:
            if l1.val<=l2.val:
                l.next=l1
                l1=l1.next
            else:
                l.next=l2
                l2=l2.next
            l=l.next
        if l1 is None:
            l.next=l2
        elif l2 is None:
            l.next=l1
        return head
