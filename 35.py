from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i,val in enumerate(nums):
            if val == target:
                return i
            elif target > nums[-1]:
                return len(nums)
            elif target < val:
                return i

print(Solution().searchInsert([1,3,5,6],7))
