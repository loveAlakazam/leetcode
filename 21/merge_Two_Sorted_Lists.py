# https://leetcode.com/problems/merge-two-sorted-lists/
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
        
        #1. l1, l2 모두다 null인 경우
        if not(l1)and not(l2):
            return l1
        #2. l1, l2 중 하나가 null인 경우
        if not(l1):
            return l2
        if not(l2):
            return l1

        #3. l1, l2 모두 null이 아닌 경우
        #head는 l1, l2 두개의 리스트를 합친 리스트의 헤더
        #curr은 l1, l2 두개의 리스트를 합친 리스트의 현재위치
        head,curr=None,None 
        curr1, curr2 = l1, l2
        
        #처음 head가 가리키는 노드를 결정
        if curr1.val<=curr2.val:
            head=curr=curr1
            curr1=curr1.next
            
        else:#curr1.val>curr2.val
            head=curr=curr2
            curr2=curr2.next
        #일단 맨앞의 노드만 취할것이기때문에, curr.next=None으로함.    
        curr.next=None
        ##################
        while (curr1 and curr2): #curr1과 curr2 가 가리키는 노드가 존재하는가?
            if curr1.val<=curr2.val:
                curr.next=curr1
                curr1= curr1.next
            else:
                curr.next=curr2
                curr2=curr2.next
            curr=curr.next
        if not(curr1): #curr1이 가리키는 노드가 존재하지않다. 리스트l1의 모든노드를 거침
            curr.next=curr2
        if not(curr2): #curr2가 가리키는 노드가 존재하지않다. 리스트l2의 모든노드를 거침
            curr.next=curr1
        return head          
