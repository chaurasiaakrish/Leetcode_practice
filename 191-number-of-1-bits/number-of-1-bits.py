class Solution:
    def hammingWeight(self, n: int) -> int:
        s = ""
        count=0
        while n > 0:
            rem = n % 2
            s += str(rem)
            n //= 2
        for i in s:
            if i=="1":
                count+=1

        return count            