# class Solution:
#     def reverseBits(self, n: int) -> int:
#         s=""
#         if n==0:
#             return 0
#         else:
#             while n>0:
#                 rem=n%2
#                 s=s+str(rem)
#                 n=n//2
#         binary=s   
#         if len(binary)<32:
#             binary=binary.zfill(32)
#         binary=binary[::-1]    
#         exp=len(binary)-1
#         summ=0
#         for i in binary:
#             summ=summ+(int(i)*2**exp)
#             exp-=1
#         return summ        
class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:].zfill(32)
        reversed_binary = binary[::-1]
        return int(reversed_binary, 2)
