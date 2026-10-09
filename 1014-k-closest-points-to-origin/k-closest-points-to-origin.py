class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        import heapq
        l2=[]
        heap=[]
        l3=[]
        for i in range(len(points)):
            dist= points[i][0]**2 + points[i][1]**2
            l2.append((dist,points[i][0],points[i][1]))
        for i in l2:
            heapq.heappush(heap,i)
        for i in range(k):
            dist,i,j=heapq.heappop(heap)
            l3.append([i,j])
        return l3  