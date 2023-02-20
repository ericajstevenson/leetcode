# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return([i,j])

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen = {}
#         for i, num in enumerate(nums):
#             if target - num in seen:
#                 return([seen[target - num],i]) # return the index for target-num in seen
#             elif num not in seen:
#                 seen[num] = i # assign num as key,  i as val

from typing import List
# brute force solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:]):
                if num + num2 == target:
                    return([i,i+j+1])

# more efficient solution, more memory intensive - hashmap!
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # value: index
        for i, num in enumerate(nums):
            if target - num in seen:
                return([seen[target - num],i])
            else:
                seen[num] = i
        return









