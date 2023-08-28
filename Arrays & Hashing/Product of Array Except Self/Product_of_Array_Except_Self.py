class Solution(object):
  def productExceptSelf(self, nums):
      map = []

      count = 1

      map.append(1)

      for i in range(len(nums) - 1):
          count *= nums[i]
          map.append(count)

      count = 1
      for i in range(len(nums) - 1, 0, -1):
          count *= nums[i]
          map[i-1] *= count
      
      return map

#Submission: https://leetcode.com/submissions/detail/1034078984/
