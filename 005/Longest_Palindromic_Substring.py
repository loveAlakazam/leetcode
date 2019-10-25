# 스스로 푼 코드가 아니다.. 다시해볼것..ㅠ!
class Solution:
    def helper(self, s, left, right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    
    def longestPalindrome(self, s: str) -> str:
        lens=len(s)
        res=""
        for i in range(lens):
            res=max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)
        return res
