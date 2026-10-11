class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        import heapq
        n=len(matrix)
        l=[]
        heap=[]
        for i in range(len(matrix)):
            for j in range(n):
                l.append(matrix[i][j])     
        for n in l:
            heapq.heappush(heap,n)
        for m in range(k):
            res=heapq.heappop(heap)
        return res       