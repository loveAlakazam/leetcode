class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.arr= nums #배열 초기화
        self.k= k
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        self.arr.append(val)
        self.arr.sort() #정렬
        return self.arr[-self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
