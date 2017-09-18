class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        r, c = click
        self._update(board, r, c)
        return board
    
    def _update(self, board, r, c):
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[r]):
            return
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return
        elif board[r][c] == 'E':
            count = self.calculate(board, r, c)
            if count == 0:
                board[r][c] = 'B'
                for i in xrange(r-1, r+2):
                    for j in xrange(c-1, c+2):
                        self._update(board, i, j)
                # self._update(board, r - 1, c)
                # self._update(board, r + 1, c)
                # self._update(board, r, c + 1)
                # self._update(board, r, c - 1)
                return
            else:
                board[r][c] = str(count)
                return
        return
            
    
    def calculate(self, board, r, c):
        result = 0
        for i in xrange(r - 1, r + 2):
            for j in xrange(c - 1, c + 2):
                if i >= 0 and i < len(board) and j >= 0 and j < len(board[r]):
                    result += (board[i][j] == 'M' or board[i][j] == 'X')
        return result
                
            
         
                
s = Solution()
a = ["EEEEEEEE","EEEEEEEM","EEMEEEEE","MEEEEEEE","EEEEEEEE","EEEEEEEE","EEEEEEEE","EEMMEEEE"]
for i in range(len(a)):
    a[i] = list(a[i])
#
#  r = s.updateBoard(board, ())
# a = [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]

r = s.updateBoard(a, (0, 0))
for i in r:
    print i