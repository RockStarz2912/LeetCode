class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize rows as a list of empty strings
        rows = ["" for _ in range(numRows)]
        curRow = 0
        goingDown = False

        # Traverse characters in zigzag pattern
        for c in s:
            rows[curRow] += c
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1

        # Concatenate all rows
        return "".join(rows)
        