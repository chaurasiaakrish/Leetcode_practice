class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for j in freq:
            if freq[j]==1:
                return j   