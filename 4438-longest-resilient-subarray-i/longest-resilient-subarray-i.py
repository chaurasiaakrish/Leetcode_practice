class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:

        low = 0
        rem = nums[0] % k
        res = 1

        for high in range(len(nums)):
            curr_rem = nums[high] % k

            if curr_rem != rem:
                low = high
                rem = curr_rem

            win_size = high - low + 1

            if ((win_size - 1) * rem) % k == 0:
                res = max(res, win_size)

        return res