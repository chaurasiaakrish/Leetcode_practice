from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}

        for i, x in enumerate(nums):
            if x not in freq:
                freq[x] = []
            freq[x].append(i)

        ans = [0] * n

        for indexes in freq.values():
            total = sum(indexes)
            left_sum = 0
            left_count = 0
            m = len(indexes)

            for i in indexes:
                right_count = m - left_count - 1
                right_sum = total - left_sum - i

                ans[i] = (
                    i * left_count - left_sum
                    + right_sum - i * right_count
                )

                left_sum += i
                left_count += 1

        return ans