# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s):
        
        s=list(s)
        head=len(s)
        closes=[]
        if len(s)==0:
            return True
        if len(s)==1:
            return False
            
        while len(s):
            if (s[-1]==')') or (s[-1]=='}') or (s[-1]==']'):
                tmp=s.pop()
                closes.append(tmp)
                continue
            if len(closes)==0 or len(s)==0:
                return False
            
            if s[-1]=='(':
                partner=')'
            elif s[-1]=='{':
                partner='}'
            elif s[-1]=='[':
                partner=']'
            
            if partner !=closes[-1]:
                return False
            else:#partner ==closes[-1]
                closes.pop()
                s.pop()
        #길이가 0이 되면..
        if len(closes)!=0:
            return False
        return True
