class NumArray(object):
    def __init__(self, nums):
        self.origin=nums
        len_origin = len(nums)
        for idx in range(1,len_origin):
            self.origin[idx]=self.origin[idx]+self.origin[idx-1]
        
        """
        :type nums: List[int]
        """

    def sumRange(self, i, j):
        if i==0:
            return self.origin[j]
        else:
            return self.origin[j]-self.origin[i-1]
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
