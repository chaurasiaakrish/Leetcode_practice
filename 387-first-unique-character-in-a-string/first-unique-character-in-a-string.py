class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq={}
        f=0
        result=float("inf")
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
        for i in range(len(s)):
            if freq[s[i]]==1:
                return i
        return -1    