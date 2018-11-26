# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head==None) or (head.next==None):
            return head
        
        notNoneNodeCnt=0   #node.next가 None이 아닌 노드의 개수
        node=head
        #마지막 노드(node.next=0)를 찾고, 전체 노드의 개수를 구한다.
        while node.next !=None:
            notNoneNodeCnt+=1
            node= node.next
        last = node #마지막 노드를 가리킴
        tmp= last.next #last.next= Null 이다.
        tail = last
        
        for c in range(1,notNoneNodeCnt+1):
            node=head
            while node.next!=tail:
                node= node.next
            target= node
            tail.next= target
            tail = target
        #for문을 거친 후의 tail.next는 null이 되어야하므로
        if(tail==head): #맨앞의 원소에 도달했는지 확인
            tail.next=tmp
        head=last
        return head
            
            
            

        
