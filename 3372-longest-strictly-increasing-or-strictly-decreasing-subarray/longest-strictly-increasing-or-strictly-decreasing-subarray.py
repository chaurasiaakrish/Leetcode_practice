class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc=1
        dec=1
        res_inc=0
        res_dec=0
        i=0
        while i<len(nums)-1:
            if nums[i+1]>nums[i]:
                inc+=1
                res_dec=max(res_dec,dec)
                dec=1
                i+=1
            elif nums[i+1]<nums[i]:
                dec+=1
                res_inc=max(res_inc,inc)
                inc=1
                i+=1    
            else:
                res_inc=max(res_inc,inc)
                res_dec=max(res_dec,dec)
                inc=1
                dec=1
                i+=1
        res_inc=max(res_inc,inc)
        res_dec=max(res_dec,dec)       
        return max(res_inc,res_dec)