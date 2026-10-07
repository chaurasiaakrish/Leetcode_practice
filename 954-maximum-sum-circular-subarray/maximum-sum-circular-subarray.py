class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)

        # Maximum subarray (normal Kadane)
        current_max = max_sum = nums[0]

        # Minimum subarray
        current_min = min_sum = nums[0]

        for num in nums[1:]:
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)

            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)

        # All numbers are negative
        if max_sum < 0:
            return max_sum

        # Non-circular vs circular
        return max(max_sum, total - min_sum)