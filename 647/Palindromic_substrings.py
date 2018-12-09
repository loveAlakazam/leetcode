# https://leetcode.com/submissions/detail/194156311/

class Solution:            
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<=1: #ex. s="", s="a"
            return len(s)
        
        #s의 문자열이 모두 동일한 문자열일 때... #s="aaa"-> palindrome-substirng개수 : 1+2+3
        sets= set(s)
        palindrome_cnt=0
        if len(sets)==1:
            for i in range(1,len(s)+1):
                palindrome_cnt+=i
            return palindrome_cnt 
        
        #len(s)>=2
        #substring을 만든다.
        subs=[]
        for i in range(1,len(s)+1): #s='aba' ,len(s)=3, i=1,2,3
            for j in range(0, len(s)-i+1):
                subs.append(s[j:j+i])
        
        
        #substring 중 palindrome인 substring을 카운트한다.
        for sub in subs:
            if (isPalindrome(sub)==True):
                palindrome_cnt+=1
        return palindrome_cnt
            
        
def isPalindrome(s):
    lens=len(s)
    if lens==1:
        return True
    
    middle = int((lens-1)/2) #가운데 원소의 인덱스
    #len(s)가 홀수인가?
    if lens%2!=0:
        left=middle-1
        right=middle+1
    #len(s)가 짝수인가?
    else: #lens%2==0
        left=middle
        right=middle+1
            
    while(left>=0 and right<=len(s)-1):
        if s[left]!=s[right]:
            return False
        left=left-1
        right=right+1
    return True
