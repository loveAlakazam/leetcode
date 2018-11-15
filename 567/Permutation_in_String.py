class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        ls1=len(s1)
        ls2=len(s2)
        if ls1>ls2:
            return False

        ss1=[0]*26 #s1 알파벳 개수
        ss2=[0]*26 #s2 알파벳 개수
        for c in s1:
            ss1[ord(c)-ord('a')]+=1
        
        #먼저 ls1길이의 문자열의 문자개수만 카운트
        for t in range(ls1):
            ss2[ord(s2[t])-ord('a')]+=1
        
        if ss1==ss2:
            return True
        
        #같지 않다면
        for i in range(ls1, ls2):
            #앞에꺼를 뺀다.
            ss2[ord(s2[i-ls1])-ord('a')]-=1
            #뒤에꺼를 더한다.
            ss2[ord(s2[i])-ord('a')]+=1
            if ss1==ss2:
                return True
        return False
