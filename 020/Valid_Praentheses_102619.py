class Solution:
    def isValid(self, s: str) -> bool:
        closes=[]
        # ), }, ] 는 stack에 넣는다.
        lens=len(s)
        top=-1
        result=True
        for i in range(lens-1,-1,-1):
            if s[i]==')' or s[i]=='}' or s[i]==']':
                closes.append(s[i])
                top+=1
                
            elif s[i]=='(' or s[i]=='{' or s[i]=='[':
                if len(closes)==0:
                    return False
                tmp =closes[top]
                if s[i]=='(' and tmp==')':
                    result=result and True
                    closes.pop()
                    top-=1
                    
                elif s[i]=='{' and tmp=='}':
                    result=result and True
                    closes.pop()
                    top-=1
                    
                elif s[i]=='[' and tmp==']':
                    result=result and True
                    closes.pop()
                    top-=1
                    
                else:
                    result=result and False
                
                    
        if top>-1:
            return False
        
        return result
        
