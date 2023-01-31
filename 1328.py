class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        mid = len(palindrome)//2

        # special case 1: single character palindromes (example 2)
        if mid == 0:
            return ""

        # special case 2: palindromes that are all (or all but 1 a's
        if palindrome[:mid].count('a') == mid:
            return palindrome[:-1] + 'b' # minimumn impact chage last a to b

        # normal case: replace first non-"a" with an "a"
        ans = list(palindrome)
        for i,c in enumerate(palindrome[:mid]):
            if c != 'a':
                ans[i] = 'a'
                break
        return "".join(ans)