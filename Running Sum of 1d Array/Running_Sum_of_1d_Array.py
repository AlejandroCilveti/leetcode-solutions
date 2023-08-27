class Solution(object):
  def runningSum(self, nums):
      output = []
      output.append(nums[0])
      for i in range(1, len(nums)):
          output.append(output[i-1] + nums[i])
      
      return output

    #Submission: https://leetcode.com/submissions/detail/1032352331/
