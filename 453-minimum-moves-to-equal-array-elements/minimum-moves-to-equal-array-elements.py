class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minn=min(nums)
        summ=0
        for i in nums:
            summ=summ+abs(i-minn)
        return summ    