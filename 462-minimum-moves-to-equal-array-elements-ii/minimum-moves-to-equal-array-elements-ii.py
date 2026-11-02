class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        summ=0
        mid = len(nums)//2
        for i in nums:
            summ=summ+abs(i-nums[mid])
        return summ