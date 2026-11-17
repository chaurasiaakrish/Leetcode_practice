class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        # 1. Precompute proper divisors for every possible substring length
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length // 2 + 1):
                if length % d == 0:
                    divisors[length].append(d)
                    
        # 2. Precompute cost[i][j] using direct index comparisons (no string creation)
        INF = 10**9
        cost = [[INF] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i + 1, n):  # Substrings must have length >= 2
                length = j - i + 1
                min_c = INF
                for d in divisors[length]:
                    cur_c = 0
                    # Check each of the 'd' interleaved groups directly via indices
                    for rem in range(d):
                        l = i + rem
                        r = j - d + 1 + rem
                        while l < r:
                            if s[l] != s[r]:
                                cur_c += 1
                            l += d
                            r -= d
                    if cur_c < min_c:
                        min_c = cur_c
                cost[i][j] = min_c

        # 3. Dynamic Programming with 1D space optimization
        # dp[i] = min changes to partition s[0..i] into 'parts' semi-palindromes
        dp = [cost[0][i] for i in range(n)]
        
        for parts in range(2, k + 1):
            new_dp = [INF] * n
            # Each semi-palindrome must have length >= 2
            for i in range(parts * 2 - 1, n):
                for h in range((parts - 1) * 2 - 1, i - 1):
                    val = dp[h] + cost[h + 1][i]
                    if val < new_dp[i]:
                        new_dp[i] = val
            dp = new_dp
            
        return dp[n - 1]
