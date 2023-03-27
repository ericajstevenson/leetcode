# solve using sliding window techique with complexity O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = 0
        charSet = set()
        l = 0

        for r in range(len(s)): # for right pointer in len s
            while s[r] in charSet: # if there is a duplicate already in charset
                charSet.remove(s[l]) # remove leftmost character
                l += 1
            charSet.add(s[r]) # add newest char on to right
            longest_substring = max(longest_substring,len(charSet))
        return longest_substring
