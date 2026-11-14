
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res = float("inf")

        for i in range(len(nums)):
            summ = 0

            for j in range(i, len(nums)):
                summ += nums[j]

                size = j - i + 1

                if l <= size <= r and summ > 0:
                    res = min(res, summ)

        return res if res != float("inf") else -1
       