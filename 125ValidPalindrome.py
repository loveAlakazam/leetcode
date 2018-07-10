class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #1. 모든 문자열을 소문자로 바꿔주기
        s = s.lower()
        
        #알파벳 소문자 리스트
        lowAlphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        # 숫자 리스트
        numbers=['0','1','2','3','4','5','6','7','8','9']
        
        #2. 알파벳 원소, 숫자만을 담는 리스트를 생성하여, 알파벳, 숫자 외 원소 제거
        onlyChar = []
        for i in s:
            for j in lowAlphabet:
                if i==j:#s의 원소 i가 알파벳이라면 리스트에 추가
                    onlyChar.append(i)
            for j in numbers:
                if i==j: #s의 원소i가 숫자라면 리스트에 추가
                    onlyChar.append(i)

        #3. left와 right가 지목한 원소가 같은지 확인, left<=right
        l=len(onlyChar)
        left = 0
        right = l-1 
        
        if l==0: # 알파벳으로 된 문자가 존재하지 않다면
            return True
        
        while left<=right:
            if onlyChar[left]==onlyChar[right]: #만약에 left와 right가 지목한 대상이 서로 같다면
                left +=1
                right-=1
            else: #만약 left와 right가 지목한 대상이 서로 다르다면
                return False
            
        #left>right 일때.. while문을 빠져나간다.
        return True
