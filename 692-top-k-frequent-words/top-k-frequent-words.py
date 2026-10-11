class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        import heapq
        l=[]
        heap=[]
        freq={}
        for i in words:
            freq[i]=freq.get(i,0)+1
        for i in freq:
            heapq.heappush(heap,(-freq[i],i))
        while heap:
            x,y=heapq.heappop(heap)
            l.append(y)
        return l[:k]    
