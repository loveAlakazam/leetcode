# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        elements=list(set(nums))
        if len(nums) == len(elements):
            return len(nums)
        
        i=1
        while(len(nums)>len(elements)):
            if nums[i-1]!=nums[i]:
                i+=1
            else:#nums[i-1]==nums[i]
                nums.pop(i)
        return len(nums)
