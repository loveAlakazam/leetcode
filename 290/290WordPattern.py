class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        #pattern은 list(pattern)으로 문자열을 단일 문자를 원소로하는 리스트로 구성 "aba" =>['a','b','a']
        p = list(pattern)
        
        #str은 split()을 이용하여 공백으로 나눠진 단어를 원소로하는 리스트로 구성 "dog cat dog"=>['dog, 'cat', 'dog']
        s = str.split()
        
        if len(p)!=len(s):
            return False
        
        #p와 s를 매칭시킨다 : 딕셔너리(dic)을 이용함. dic['pattern'] ='str'
        dic ={}
        for i in range(0,len(p)):
            dic[p[i]]=s[i]
        
        #딕셔너리를 만든걸 바탕으로 pattern에 따라 latest 리스트 작성
        latest=[]
        for i in range(0,len(p)):
            nowPattern = p[i]
            for j in dic:
                if j==nowPattern:
                    latest.append(dic[j])
                    
        for i in range(0,len(latest)):
            if s[i]!=latest[i]:
                return False
        return True
            
            
        
        
        
            
        
