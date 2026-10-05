class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        a2=float("inf")
        a1=float("-inf")
        summ=0
        i=0
        j=i+1
        nums.sort()
        k=len(nums)-1
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                summ=nums[i]+nums[j]+nums[k]
                if summ<target:
                    a1=max(a1,summ)
                    j+=1
                else:
                    a2=min(a2,summ)
                    k-=1

        res1=abs(target-a1)
        res2=abs(target-a2)
        if res1>res2:
            return a2
        else:
            return a1            
