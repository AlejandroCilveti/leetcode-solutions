class Solution(object):
  def groupAnagrams(self, strs):
      map = defaultdict(list)

      for s in strs:
          charachters = [0] * 26
          for c in s:
              charachters[ord(c) - ord("a")] += 1
          map[tuple(charachters)].append(s)
      
      return map.values()

#Submission: https://leetcode.com/submissions/detail/1033361290/
