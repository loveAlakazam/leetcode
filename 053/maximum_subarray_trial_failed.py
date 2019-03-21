class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return None
        if len(nums)==1:
            return nums[0]
        #원소가 1개인 것들 중에서 가장 큰값/ 모든 원소의 합
        max_sum=max( max(nums), sum(nums))
        
        for cnt in range(2,len(nums)):
            for i in range(len(nums)-cnt+1):
                k=sum(nums[i:i+cnt])
                if k>max_sum:
                    max_sum=k
        return max_sum
