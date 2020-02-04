class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g와 s를 오름차순으로 정렬
        g=sorted(g)
        s=sorted(s)
        
        lens= len(s)
        leng= len(g)
        result=0
        i,j=0,0
        while i<leng and j<lens:
            if g[i]<=s[j]:
                result+=1
                i+=1
                j+=1
                
            else: #g[i]>s[j]
                j+=1         
        return result
