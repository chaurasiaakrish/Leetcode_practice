class Solution:
    def isHappy(self, n: int) -> bool:
        fast=n
        slow=n
        def digit(n):
            sq=0
            while n>0:
                rem=n%10
                sq=sq+rem*rem
                n=n//10
            return sq
        while fast!=1:
            slow=digit(slow)
            fast=digit(digit(fast))
            if (fast==slow and slow!=1):
                return False
        return True        