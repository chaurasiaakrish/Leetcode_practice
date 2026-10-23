class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        string=[]
        for i in s:
            if i.isalnum():
                string.append(i)
        string="".join(string)        
        if len(string)==0:
            return True
        else:
            j=0;k=len(string)-1 
            while j<=k:
                if string[j]==string[k]:
                    j+=1
                    k-=1
                else:
                    return False
        return True            