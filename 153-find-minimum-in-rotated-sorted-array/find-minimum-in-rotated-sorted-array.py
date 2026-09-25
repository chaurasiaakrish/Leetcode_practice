class Solution:
    def findMin(self, nums: list[int]) -> int:
        ans=float("inf")
        left =0
        right = len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                ans=min(ans,nums[mid])
                left=mid+1
            else:
                ans=min(ans,nums[mid])
                right=mid-1    
        return ans        