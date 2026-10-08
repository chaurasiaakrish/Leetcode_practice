class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(high+low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[low]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1    

        return -1        