class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        import heapq
        freq={}
        heap=[]
        l=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for j in freq:
            heapq.heappush(heap,(-freq[j],j))
        for m in range(k):
            a,b=heapq.heappop(heap)
            l.append(b)
        return l    