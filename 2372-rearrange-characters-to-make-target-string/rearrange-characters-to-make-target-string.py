class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        count=0
        res=float("inf")
        s_freq={}
        tar_freq={}
        for i in range(len(s)):
            s_freq[s[i]]=s_freq.get(s[i],0)+1
        for j in range(len(target)):
            tar_freq[target[j]]=tar_freq.get(target[j],0)+1
        for char in tar_freq:
            count=s_freq.get(char,0)//tar_freq[char]
            res=min(res,count)
        return res     