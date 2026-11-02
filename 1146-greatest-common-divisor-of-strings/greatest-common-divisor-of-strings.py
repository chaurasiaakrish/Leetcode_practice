class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        k=self.find_gcd(len(str1),len(str2))
        x=str1[:k]
        if (str1 == x * (len(str1) // k) and
            str2 == x * (len(str2) // k)):
            return x

        return "" 
    def find_gcd(self,a,b):
        while b:
            a,b=b,(a%b)    
        return a    