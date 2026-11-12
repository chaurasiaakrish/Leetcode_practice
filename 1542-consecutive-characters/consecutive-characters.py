class Solution:
    def maxPower(self, s: str) -> int:
        res=0
        count=1
        i=0
        while i <len(s)-1:
            if s[i]==s[i+1]:
                count+=1
                i+=1
            else:
                res=max(res,count)
                count=1
                i+=1    
        res=max(res,count)
        return res        