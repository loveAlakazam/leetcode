class Solution:
    def isPowerOfThree(self, n):
        if n==0:
            return False
        
        while n%3==0: #n은 3에 나누어떨어지는 수
            n=n//3 #이전n을 3으로 나눈 몫의 값으로 갱신
            
        #3의 제곱수의 마지막 n=1일때
        #3의 제곱수라면.. 몫은 0, 나머지는 1
        if n//3==0 and n%3==1:
            return True
        else:  #n=1이 아닌수는 무조건 false
            return False
