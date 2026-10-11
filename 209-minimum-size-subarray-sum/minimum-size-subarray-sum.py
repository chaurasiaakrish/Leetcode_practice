class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:        
        hire=0
        fire=0
        summ=0
        result=float("inf")
        for hire in range(len(nums)):
            summ=summ+ nums[hire]
            while summ>=target:
                length=hire-fire+1
                result=min(result,length)
                summ=summ-nums[fire]
                fire+=1
        if result==float("inf"):
            return 0
        else:
            return result     

