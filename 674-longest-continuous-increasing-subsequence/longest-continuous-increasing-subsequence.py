class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        inc=1
        strict=0
        i=0
        while i<len(nums)-1:
            if nums[i+1]>nums[i]:
                inc+=1
                i+=1
            else:
                strict=max(strict,inc)
                inc=1
                i+=1
        strict=max(strict,inc)
        return strict             