class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j=0
        summ=0
        result=float("inf")  #max number
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
