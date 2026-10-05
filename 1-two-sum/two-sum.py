
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        freq = {}

        for i in range(len(nums)):
            var = target - nums[i]

            if var in freq:
                return [freq[var], i]

            freq[nums[i]] = i

        return []             