class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        import heapq
        if len(stones)==1:
            return stones[0]
        else:
            heap=[]
            for i in stones:
                heapq.heappush(heap,-i)
            while heap:
                if len(heap)>1:
                    x=-heapq.heappop(heap)
                    y=-heapq.heappop(heap)
                    if x==y:
                        continue
                    else:
                        heapq.heappush(heap,(y-x))
                elif len(heap)==0:
                    return 0   
                elif len(heap)==1:
                        return -heap[0]        
        if len(heap)==0:
            return 0   
        else:
            return -heap[0]        
           