class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans_map={}
        mag_map={}
        for i in range(len(ransomNote)):
            rans_map[ransomNote[i]]=rans_map.get(ransomNote[i],0)+1
        for j in range(len(magazine)):
            mag_map[magazine[j]]=mag_map.get(magazine[j],0)+1
        for char in rans_map:
            if mag_map.get(char,0)<rans_map[char]:
                return False
        return True        