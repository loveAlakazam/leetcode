class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #문자열의 길이가 서로 다른가?
        if len(s) != len(t):
            return False
        else: #두 문자열의 길이가 서로 같다.
            s1 = []
            t1 = []
            for i in range(0,len(s)):
                s1.append(s[i])
                t1.append(t[i])
            #순서대로 sort 시킨다.
            s1.sort()
            t1.sort()
            for i in range(0,len(s1)):
                if s1[i]!=t1[i]: #i번째에 서로 다르다면..
                    return False
            return True
            
            
