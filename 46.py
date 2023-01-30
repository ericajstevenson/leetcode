
class Solution:
    def __init__(self):
        self.res = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, [])
        return self.res
    def backtrack(self, nums, path):
        if not nums: # if nums is empty (used in next for loop)
            self.res.append(path)
        for x in range(len(nums)):
            self.backtrack(nums[:x]+nums[x+1:],path+[nums[x]])

