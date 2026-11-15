class Solution:
  def numOfSubarrays(self, arr: list[int]) -> int:
    MOD = 10**9 + 7
    ans = 0
    s = 0
    cnt = [1, 0]  # cnt[0] for even prefix sums, cnt[1] for odd prefix sums

    for x in arr:
      s += x
      ans = (ans + cnt[s & 1 ^ 1]) % MOD
      cnt[s & 1] += 1

    return ans

        