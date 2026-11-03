class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minn=max(nums)
        summ=0
        for i in nums:
            summ=summ+abs(minn-i)
        return summ    