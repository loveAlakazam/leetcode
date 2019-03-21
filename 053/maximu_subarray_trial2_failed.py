class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def find_left_max(nums, max_sum):
            sum=0
            for i in range(len(nums)-1,-1,-1):
                sum+=nums[i]
                if sum>max_sum:
                    max_sum=sum
            return max_sum
        
        def find_right_max(nums, max_sum):
            sum=0
            for i in range(len(nums)):
                sum+=nums[i]
                if sum>max_sum:
                    max_sum=sum
            return max_sum
        
        def find_both_max(max_idx, max_sum):
            if max_idx==0:#맨왼쪽에 위치
                return find_right_max(nums,max_sum)
            
            elif max_idx==len(nums)-1:#맨오른쪽에 위치
                return find_left_max(nums,max_sum)
            
            else:
                sum=nums[max_idx]
                left=max_idx-1
                right=max_idx+1
                while left>=0 and right<len(nums):
                    sum+=(nums[left]+nums[right])
                    if sum>max_sum:
                        max_sum=sum
                    left-=1
                    right+=1
                return max_sum
                
            
        if len(nums)==0:
            return None
        if len(nums)==1:
            return nums[0]
        
        max_idx=nums.index(max(nums))
        max_sum=nums[max_idx]
        
        #left_group=nums[:max_idx+1]
        #right_group=nums[max_idx:]
        left_max=find_left_max(nums[:max_idx+1], max_sum)
        right_max=find_right_max(nums[max_idx:], max_sum)
        both_max=find_both_max(max_idx, max_sum)
        return max(left_max, right_max, both_max)
