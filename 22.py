class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN,closedN):
            if openN == closedN == n: # if all the parentheses are there
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
        backtrack(0,0) # call backtrack starting at 0
        return res
