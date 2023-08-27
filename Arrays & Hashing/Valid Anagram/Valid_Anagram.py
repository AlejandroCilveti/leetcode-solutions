class Solution(object):
  def isAnagram(self, s, t):
      map_s, map_t = {}, {}

      if len(s) != len(t): return False

      for i in range(len(s)):
          map_s[s[i]] = 1 + map_s.get(s[i], 0)
          map_t[t[i]] = 1 + map_t.get(t[i], 0)
      
      for x in map_s:
          if map_s[x] != map_t.get(x, 0): return False

      return True

#Submission: https://leetcode.com/submissions/detail/1033117490/
