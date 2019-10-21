class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        
        dp1=[n for n in nums]
        dp2=[n for n in nums]
        
        #dp1은 맨첫번째집을 방문할 수 있다.
        dp1[0]=nums[0]
        dp1[1]=max(nums[0], nums[1])
        
        #dp2는 맨첫번째집을 방문할 수 없다
        dp2[0]=0
        
        for i in range(2, len(nums)):
            dp1[i]=max(dp1[i-1], dp1[i-2]+dp1[i])
            dp2[i]=max(dp2[i-1], dp2[i-2]+dp2[i])
        return max(dp2[-1], dp1[-2])
