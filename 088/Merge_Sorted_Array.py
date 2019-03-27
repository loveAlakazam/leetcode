class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums1)==0: #nums1=[]
            nums1=nums2
        
        if len(nums1)>0 and len(nums2)>0:
            #num1에 nums2의 원소 num2를 넣는다.
            for num2 in nums2:
                nums1.append(num2)
            nums1.sort()
            
            while len(nums1)>(m+n):# 두개의 array를 합친 결과 nums1의 길이가 m+n보다 크면 nums1의 원소 0을 지운다.
                nums1.remove(0)
