# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=1
        right=n
        while(left<=right):
            middle= (left+right)//2
            if guess(middle)==0:# middle==pick
                return middle
            elif guess(middle)==1:# middle<pick
                left=middle+1
            else:# middle>pick
                right=middle-1
