class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        summ=0
        i=len(a)-1
        j=len(b)-1
        s=""
        while i>=0 or j>=0:
            x=a[i] if i>=0 else 0
            y=b[j] if j>=0 else 0    
            summ=int(x)+int(y)+carry
            digit=summ%2
            s=s+str(digit)
            carry=summ//2
            i-=1
            j-=1
        if carry!=0:
            s=s+str(carry)    
        return s[::-1]    