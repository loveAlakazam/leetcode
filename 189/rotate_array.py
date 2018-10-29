class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=0
        while(i<k):
            #맨마지막 원소를 뽑는다.
            add1= nums.pop()
            #맨마지막 원소를 0번째 인덱스에 insert시킨다.
            nums.insert(0,add1)
            #카운트
            i+=1
