"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that
nums[i] == nums[j] and abs(i - j) <= k.
 """
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)): # if there are no duplicates in the list
            return False
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k and i != j:
                    return True
        return False

# print(Solution.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))

