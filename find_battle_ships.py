class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j].lower() == 'x':
                    # combining i,j=0 or if i=0 & left is not x or j=0 & top is not x or
                    # when i,j !=0 (>0) and left or right is not x
                    if (i == 0 or (i > 0 and board[i-1][j].lower() != 'x')) and \
                            (j == 0 or (j > 0 and board[i][j-1].lower() != 'x')):
                        count += 1
        return count





