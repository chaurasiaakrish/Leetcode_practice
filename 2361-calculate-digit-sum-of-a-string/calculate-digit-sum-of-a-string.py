class Solution:
  def digitSum(self, s: str, k: int) -> str:
    while len(s) > k:
      next_groups = []
      for i in range(0, len(s), k):
        group = s[i : i + k]
        digit_sum = sum(int(ch) for ch in group)
        next_groups.append(str(digit_sum))
      s = "".join(next_groups)
    return s
            



