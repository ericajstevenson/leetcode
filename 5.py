class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # check odd length palindromes
            l, r  = i, i # initialize both left and right ptrs to center position i
            while l >= 0 and r < len(s) and s[l] == s[r]: # while l and r in bounds
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1

            # check even length palindromes
            l, r = i, i+1  # initialize both left and right ptrs to center position i
            while l >= 0 and r < len(s) and s[l] == s[r]:  # while l and r in bounds
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1

        return res


