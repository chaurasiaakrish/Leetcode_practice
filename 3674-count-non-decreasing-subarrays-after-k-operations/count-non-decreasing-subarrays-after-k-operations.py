from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        dq = deque()
        cost = 0
        ans = 0

        j = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            count = 1

            # Merge smaller groups into the current value
            while dq and dq[-1][0] < num:
                next_num, next_count = dq.pop()

                count += next_count
                cost += (num - next_num) * next_count

            dq.append((num, count))

            # Shrink the window while cost exceeds k
            while cost > k:
                rightmost_num, rightmost_count = dq.popleft()

                cost -= rightmost_num - nums[j]
                j -= 1

                if rightmost_count > 1:
                    dq.appendleft((rightmost_num, rightmost_count - 1))

            # Count all valid subarrays ending at positions i through j
            ans += j - i + 1

        return ans
