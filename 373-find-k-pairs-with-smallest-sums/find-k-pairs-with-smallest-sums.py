class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        import heapq

        if not nums1 or not nums2 or k == 0:
            return []

        heap = []
        result = []

        for j in range(min(k, len(nums2))):
            heapq.heappush(heap, (nums1[0] + nums2[j], 0, j))

        while heap and len(result) < k:
            summ, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])

            if i + 1 < len(nums1):
                heapq.heappush(
                    heap,
                    (nums1[i + 1] + nums2[j], i + 1, j)
                )

        return result
        