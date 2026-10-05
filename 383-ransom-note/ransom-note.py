class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans_freq={}
        mag_freq={}
        flag=False
        for i in ransomNote:
            rans_freq[i]=rans_freq.get(i,0)+1
        for i in magazine:
            mag_freq[i]=mag_freq.get(i,0)+1    
        for i in rans_freq:
            if mag_freq.get(i,0)>=rans_freq.get(i,0):
                continue
            else:
                return False
        return True                  