class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        i = 0

        while i < len(words):
            line = []
            line_length = 0

            # 1. Collect as many words as possible
            while i < len(words):
                word_len = len(words[i])

                if line_length + word_len + len(line) > maxWidth:
                    break

                line.append(words[i])
                line_length += word_len
                i += 1

            # 2. Last line OR line containing only one word
            if i == len(words) or len(line) == 1:
                result.append(" ".join(line).ljust(maxWidth))
                continue

            # 3. Distribute spaces
            total_spaces = maxWidth - line_length
            gaps = len(line) - 1

            spaces = total_spaces // gaps
            extra = total_spaces % gaps

            current_line = ""

            for j in range(gaps):
                current_line += line[j]
                current_line += " " * spaces

                if j < extra:
                    current_line += " "

            current_line += line[-1]
            result.append(current_line)

        return result