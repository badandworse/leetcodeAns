class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        if not board:
            return False
        
        rows=len(board)
        cols=len(board[0])
        for i in range(rows):
            for j in range(cols):
                if self.findPath(board,rows,cols,i,j,word):
                    return True
        
        return False
    
    def findPath(self,board,rows,cols,row,col,word):
        if len(word)==0:
            return True
        if 0<=row<rows and 0<=col<cols and board[row][col]!='-1':
            if board[row][col]==word[0]:
                temp=board[row][col]
                board[row][col]='-1'
                newWord=word[1:]
                result=self.findPath(board,rows,cols,row+1,col,newWord) or self.findPath(board,rows,cols,row-1,col,newWord)\
                or self.findPath(board,rows,cols,row,col-1,newWord) or self.findPath(board,rows,cols,row,col+1,newWord)
                if result:
                    return True
                board[row][col]=temp
        return False