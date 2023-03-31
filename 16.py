class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        closest = 100000
        nums.sort()

        for i, val in enumerate(nums):
            if i>0 and val == nums[i-1]: # if i is not the first number and it's not a repeated value
                continue

            l,r = i+1,len(nums)-1
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum == target:
                    return threeSum
                elif abs(threeSum - target) < abs(closest - target):
                    closest = threeSum
                elif threeSum <= target:
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
        return closest







