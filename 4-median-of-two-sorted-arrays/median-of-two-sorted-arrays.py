class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i=0
        j=0
        l=[]
        while i<=len(nums1)-1 and j<=len(nums2)-1:
            if nums1[i]<nums2[j]:
                l.append(nums1[i])
                i+=1
            else:
                l.append(nums2[j])
                j+=1
        while i <=len(nums1)-1:
                l.append(nums1[i])
                i+=1
        while j<=len(nums2)-1:
                l.append(nums2[j]) 
                j+=1
        if len(l)>0 and len(l)%2==0:
            rem=len(l)//2
            rem1=l[rem-1]
            rem2=l[rem]
            median=(rem1+rem2)/2
        elif len(l)==0:
            return 0
        else:
            rem=len(l)//2
            median=l[rem]
        return float(median)        