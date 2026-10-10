class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0

        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    count += 1

        return count + len(stack)       