class Solution(object):
  def isValidSudoku(self, board):
      rows = collections.defaultdict(set)
      columns = collections.defaultdict(set)
      groups = collections.defaultdict(set)

      for r in range(9):
          for c in range(9):
              if board[r][c] == ".":
                  continue
              if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in groups[(r//3, c//3)]:
                  return False
              rows[r].add(board[r][c])
              columns[c].add(board[r][c])
              groups[(r//3, c//3)].add(board[r][c])
      return True 
    
#Submission: https://leetcode.com/submissions/detail/1034520926/
