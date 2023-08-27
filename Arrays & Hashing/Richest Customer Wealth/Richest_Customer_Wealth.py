class Solution(object):
  def maximumWealth(self, accounts):
      max_wealth = 0

      for i in range(len(accounts)):
          wealth = 0
          for j in range(len(accounts[0])):
              wealth = wealth + accounts[i][j]

          if wealth > max_wealth:
              max_wealth = wealth
      
      return max_wealth

#Submission: https://leetcode.com/submissions/detail/1032379467/
