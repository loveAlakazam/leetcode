class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenn=len(nums)
        if lenn==0:
            return 0
        
        elif lenn==1:
            return nums[0]
        
        elif lenn>=2:
            c= [0]* lenn
            c[0]=nums[0]
            for target in range(1,lenn):
                if target==1:
                    c[target]=max(nums[target], nums[target-1])
                else:
                    c[target]=nums[target]+max(c[:target-1])
            return max(c)
