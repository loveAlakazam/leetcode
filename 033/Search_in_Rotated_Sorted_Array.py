class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #오름차순으로 sort 시킨다.
        nums2=sorted(nums)
        left=0
        right=len(nums)-1
        while(left<=right):
            middle=(left+right)//2
            if nums2[middle]==target:
                return nums.index(target)
            elif nums2[middle]>target:
                right= right-1
            else: #nums[middle]<target
                left= left+1
        return -1
        
