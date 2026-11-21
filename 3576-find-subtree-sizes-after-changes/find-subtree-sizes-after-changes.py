from typing import List
import sys

# Increase recursion depth for deep trees (up to 10^5 nodes)
sys.setrecursionlimit(200000)


class Solution:

  def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
    n = len(parent)
    adj = [[] for _ in range(n)]
    for i in range(1, n):
      adj[parent[i]].append(i)

    new_parent = list(parent)
    # Tracks the closest ancestor seen so far for each lowercase letter ('a' to 'z')
    last_seen = [-1] * 26

    # Pass 1: Find the new parent for every node simultaneously via DFS + backtracking
    def find_new_parents(u: int) -> None:
      char_idx = ord(s[u]) - ord('a')
      if last_seen[char_idx] != -1:
        new_parent[u] = last_seen[char_idx]

      # Save previous state, update current node as closest ancestor, and recurse
      prev_ancestor = last_seen[char_idx]
      last_seen[char_idx] = u

      for v in adj[u]:
        find_new_parents(v)

      # Backtrack so sibling branches don't see this node as an ancestor
      last_seen[char_idx] = prev_ancestor

    find_new_parents(0)

    # Build the restructured tree using new_parent
    new_adj = [[] for _ in range(n)]
    for i in range(1, n):
      new_adj[new_parent[i]].append(i)

    # Pass 2: Calculate subtree sizes on the updated tree
    ans = [1] * n

    def count_sizes(u: int) -> int:
      for v in new_adj[u]:
        ans[u] += count_sizes(v)
      return ans[u]

    count_sizes(0)
    return ans
