from typing import List

# BRUTE FORCE solution
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_area = 0
#         for i in range(len(height)):
#             for j in range(i+1, len(height)):
#                 max_area = max(max_area,min(height[i],height[j])*(j-i))
#                 # print(max_area)
#         return max_area



# OPTIMIZED solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l,r = 0,len(height)-1
        while l < r:
            max_area = max(max_area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


s=Solution()
print(s.maxArea([9,8,6,2,5,4,9,8,1]))
