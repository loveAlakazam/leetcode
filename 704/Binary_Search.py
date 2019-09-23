class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right=0 , len(nums)-1 #왼쪽끝(0), 오른쪽끝( len(nums)-1 )
        while(left<=right):
            middle= (left+right)//2
            if nums[middle]==target: #middle에서 target을 찾음
                return middle
            elif nums[middle]<target:
                left=middle+1
            else:# nums[middle]>target
                right=middle-1
            
        return -1 #target이 nums에 없는 경우
