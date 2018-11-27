# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head) or not(head.next):
            return head
        curr=head
        while curr.next:#curr.next가 존재한다.
            if curr.val==curr.next.val:
                if not(curr.next.next): #curr.next.next가 null이라면
                    curr.next=None
                else:
                    curr.next=curr.next.next
            else:
                curr=curr.next
        return head
