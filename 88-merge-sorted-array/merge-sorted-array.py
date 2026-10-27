class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l=[]
        i=0;j=0
        while i<m and j < n:
            if nums1[i]<=nums2[j]:
                l.append(nums1[i])
                i+=1
            else:
                l.append(nums2[j])  
                j+=1
        while i<m:
                l.append(nums1[i])
                i+=1
        while j<n:
                l.append(nums2[j])
                j+=1     
        for i in range(m+n):
            nums1[i]=l[i]            