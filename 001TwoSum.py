class Solution:
    def twoSum(self, nums, target):
        result = []
        for i in nums:
            first = i
            fi= nums.index(i)
            test = target - first
            for second in range(fi+1, len(nums)):
                if nums[second]==test:
                    result.append(nums.index(first))
                    result.append(second)
                    return result
        return result
                    
                
        
        
        
        
    
                
                
        
        
            

    
    
            
