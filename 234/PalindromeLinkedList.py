#문제: https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not (head): #input : []
            return True
        if not (head.next):#input: [1]
            return True
        
        a=[]
        curr=head
        while curr.next: #curr.next !=Null
            a.append(curr.val)
            curr= curr.next
        a.append(curr.val) #마지막노드의 val값을 넣는다.
        len_a =len(a)
        
        m=int((len_a -1)/2) #가운데 인덱스
        if len_a %2==0: #a의 길이가 짝수라면
            left=m
            right=m+1
        else: #a의 길이가 홀수라면
            left=right=m
        while (left>=0) and (right<len_a):
            if a[left]!= a[right]:
                return False
            else: #a[left]==a[right]
                left -=1
                right+=1
        return True
        
        
