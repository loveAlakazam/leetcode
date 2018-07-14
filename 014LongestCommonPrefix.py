class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #리스트 안의 단어가 존재하지 않다면
        if len(strs)==0:
            return ""
        #리스트 안의 단어가 1개라면 => 1개 통째로 리턴
        elif len(strs)==1:
            return strs[0]
        
        #리스트 안의 단어가 2개 이상이라면
        #1. 리스트 안의 단어중 가장 짧은 단어의 길이 구하기
        shortest = len(strs[0]) #처음에는 strs[0]의 단어길이로 초기화
        for i in strs:
            if len(i)<shortest:
                shortest=len(i)
                
        result=[] #모든 단어가 공통으로 같은 원소들을 모으는 리스트, 비어있는 리스트로 초기화
        sameCount=1 #공통원소 카운트
        #2. 0번째 단어의 원소를 기준으로 1~len(strs)개의 단어들의 0~가장짧은단어길이-1 번째 원소가 같은지 비교
        for i in range(0,shortest): #단어의 0번째~shortest-1 번째 원소까지 비교
            compare = strs[0][i] #0번째 단어의 i번째(0~shortest-1) 원소를 기준으로하여..
            for j in range(1,len(strs)): #compare와 1번째 단어~ len(strs)-1 번째 단어의 i번째 원소가 서로 같은지 비교
                if strs[j][i]==compare: #compare와 같다면 sameCount를 1추가
                    sameCount+=1

            #맨앞의 원소가 서로  다르다면 굳이 뒷부분이 같더라도 무시한다.
            #""로 리턴한다.
            if i==0 and sameCount!=len(strs):
                return ""
            
            #sameCount가 리스트에 등록된 단어의 개수와 같으면 => result리스트에 compare를 append
            if sameCount==len(strs):
                result.append(compare)
            sameCount=1 #다시 초기화
                    
            
        #결과 리스트(result)를 문자열로 바꾸기
        result=''.join(result)
        return result
