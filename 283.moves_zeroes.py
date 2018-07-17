class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
       
        #0의 개수 카운트
        countZero =0 #0의 개수
        #원래 nums의 길이
        originLen = len(nums)
        
        for i in range(0,originLen):
            if nums[i]==0: #nums[i]가 0이라면
                nums.append(0)
                countZero+=1
                
        for i in range(0,countZero):#0의 개수만큼 앞의 zero 지우기
            nums.remove(0)
        
            
        
        
        
