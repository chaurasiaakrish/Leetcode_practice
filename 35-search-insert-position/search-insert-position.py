from bisect import bisect_left
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        index=bisect_left(nums,target)
        return index