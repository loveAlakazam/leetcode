class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        S=S.replace('()','.')
        lens=len(S)
        output=""
        
        right_case_idx=[]
        top=lens-1
        while(top>0):
            now=S[top]
                
            if now==')':#right_case_idx에 넣는다.
                if len(right_case_idx)>0:
                    output+=now
                right_case_idx.append(top)
                    
            elif now=='(': #right_case_idx를 뺀다.
                right_case_idx.pop()
                if len(right_case_idx)>0:
                    output+=now
                
            else:#now=='.'
                if len(right_case_idx)>0:
                    output+=now   
            top-=1
            
        output=output[::-1]
        output=output.replace('.','()')
        return output
