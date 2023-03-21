class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        output = [""]
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        for i in digits:
            tmp = []
            for j in d[i]:
                for k in output:
                    tmp.append(k + j)
            output = tmp
        return output

# recursive solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        output = []
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        def backtrack(i, curStr):
            # base case if reached the end of string
            if len(curStr) == len(digits):
                output.append(curStr)
                return

           for c in d[digits[i]]:
                backtrack(i + 1, curStr + c)

