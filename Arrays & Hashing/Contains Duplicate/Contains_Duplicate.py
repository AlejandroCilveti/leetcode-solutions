class Solution(object):
  def containsDuplicate(self, nums):
      map = {}
      for i, n in enumerate(nums):
          if n in map:
              return [map[n], i]
          map[n] = i

#Submission: https://leetcode.com/submissions/detail/1032414858/
