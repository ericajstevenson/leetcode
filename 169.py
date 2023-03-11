# less efficient solution - hashmap
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxCount = 0, 0
        for num in nums:
            count[num] = 1 + count.get(num, 0) # return 0 if n is not in count
            if count[num] > maxCount:
                maxCount = count[num]
                res = num
        return res

# much better, given the problem constraints
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority = 0
        for num in nums:
            if count == 0:
                majority = num
            count += (1 if num == majority else -1)
        return majority
