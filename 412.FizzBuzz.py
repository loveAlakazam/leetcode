class Solution:
    def fizzBuzz(self, n):
        '''
        3의배수: Fizz
        5의배수: Buzz
        3과 5의 최소공배수: FizzBuzz
        '''
        l=[]
        for i in range(1,n+1): #1~n
            if i%3==0 and i%5==0:
                l.append('FizzBuzz')
            elif i%3==0:
                l.append('Fizz')
            elif i%5==0:
                l.append('Buzz')
            else:
                l.append(str(i))
        return l
