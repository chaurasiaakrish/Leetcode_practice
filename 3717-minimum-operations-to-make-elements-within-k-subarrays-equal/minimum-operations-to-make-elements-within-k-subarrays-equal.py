class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        import heapq
from collections import defaultdict

class DualHeap:
    def __init__(self):
        self.small = []       # Max heap (stored as negative values)
        self.large = []       # Min heap
        self.delayed = defaultdict(int)

        self.small_size = 0
        self.large_size = 0

        self.small_sum = 0
        self.large_sum = 0

    def prune(self, heap):
        while heap:
            num = -heap[0] if heap is self.small else heap[0]

            if self.delayed[num] > 0:
                heapq.heappop(heap)
                self.delayed[num] -= 1
            else:
                break

    def balance(self):
        if self.small_size > self.large_size + 1:
            self.prune(self.small)
            num = -heapq.heappop(self.small)

            heapq.heappush(self.large, num)
            self.small_size -= 1
            self.large_size += 1
            self.small_sum -= num
            self.large_sum += num

            self.prune(self.small)

        elif self.small_size < self.large_size:
            self.prune(self.large)
            num = heapq.heappop(self.large)

            heapq.heappush(self.small, -num)
            self.large_size -= 1
            self.small_size += 1
            self.large_sum -= num
            self.small_sum += num

            self.prune(self.large)

    def add(self, num):
        self.prune(self.small)

        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
            self.small_sum += num
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
            self.large_sum += num

        self.balance()

    def remove(self, num):
        self.prune(self.small)
        self.prune(self.large)

        self.delayed[num] += 1

        if num <= -self.small[0]:
            self.small_size -= 1
            self.small_sum -= num

            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            self.large_sum -= num

            if self.large and num == self.large[0]:
                self.prune(self.large)

        self.balance()

    def get_cost(self):
        self.prune(self.small)

        median = -self.small[0]

        left_cost = median * self.small_size - self.small_sum
        right_cost = self.large_sum - median * self.large_size

        return left_cost + right_cost


class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)

        # Step 1: Calculate the cost of every window of size x
        dh = DualHeap()
        costs = []

        for i in range(n):
            dh.add(nums[i])

            if i >= x:
                dh.remove(nums[i - x])

            if i >= x - 1:
                costs.append(dh.get_cost())

        # Step 2: Dynamic Programming
        INF = float('inf')

        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, min(k, i // x) + 1):

                # Option 1: Skip current element
                dp[i][j] = dp[i - 1][j]

                # Option 2: Select a window of size x
                if i >= x:
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i - x][j - 1] + costs[i - x]
                    )

        return dp[n][k]