# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# 나의 풀이
# nums=[1,2,3,4] , elements=[1,2,3,4] 
# len(nums) == len(elements) 이므로 그냥 len(elements)를 리턴

# nums=[1,1,1,2,2,3] , elements=[1,2,3]
# len(nums)>len(elements) 라면
# i=1 부터 시작. nums[i-1]와 nums[i]가 서로 같으면 nums[i]를 제거.
# 1) nums[1]은 nums[0]과 같으므로 nums.pop(1)
# nums=[1,(1),1,2,2,3]  --> nums=[1,1,2,2,3]
# 2) nums[1]은 nums[0]과 같으므로.. nums.pop(1)
# nums=[1,(1),2,2,3] --> nums=[1,2,2,3]
# 3) nums[1]과 nums[0]은 서로 다르므로 i=1 --> i=2
# nums=[1,(2),2,3]
# 4) nums[2]와 nums[1]는 서로 같으므로 nums.pop(2)
# nums=[1,2,(2),3] --> nums=[1,2,3]

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
