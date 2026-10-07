class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=""
        for i in s.lower():
            if i.isalnum():
                t=t+i
            else:
                continue 
        j=0
        k=len(t)-1
        while j<k:
            if t[j]==t[k]:
                j+=1
                k-=1
            else:
                return False     
        return True           
        