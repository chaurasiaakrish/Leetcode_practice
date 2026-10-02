class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        l = []

        for j in range(len(strs[0])):
            for i in range(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != strs[0][j]:
                    return "".join(l)

            l.append(strs[0][j])

        return "".join(l)