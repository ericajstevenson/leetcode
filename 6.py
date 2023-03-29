class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = ""
        cycle = 2 * numRows - 2
        for i in range(numRows):
            for j in range(i, len(s), cycle):
                res += s[j]
                k = j + cycle - 2 * i
                if i != 0 and i != numRows - 1\
                        and k < len(s):
                    res += s[k]
        return res




