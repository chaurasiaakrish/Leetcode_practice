class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ=0
        j=0
        result=float("inf")
        for i in range(len(nums)):
            summ=summ+nums[i]
            while summ>=target:
                size=i+1-j
                result=min(result,size)
                summ=summ-nums[j]
                j+=1
        if result==float("inf"):
            return 0
        else:
            return result    


