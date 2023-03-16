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


