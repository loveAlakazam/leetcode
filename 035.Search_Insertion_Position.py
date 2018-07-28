class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        insertTarget=0 #타겟이 넣어야할 인덱스번호
        for i in range(len(nums)):
            if target > nums[i]:
                insertTarget+=1
            else:#target<= nums[i]
                break
        
        #insertTarget에 target을 넣는다
        nums.insert(insertTarget,target)
        return nums.index(target)
 
 
        
