class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowfill=[[False for i in range(9)] for i in range(9)];
        colfill=[[False for i in range(9)] for i in range(9)];
        squfill=[[False for i in range(9)] for i in range(9)];
        for i in range(9):
            for j in range(9):
                if(board[i][j]=="."):
                    continue;
                value=int(board[i][j])-1;
                if(rowfill[i][value]):
                    return False;
                else:
                    rowfill[i][value]=True;
                if(colfill[j][value]):
                    return False;
                else:
                    colfill[j][value]=True;
                if(squfill[(i/3)*3+j/3][value]):
                    return False;
                else:
                    squfill[(i/3)*3+j/3][value]=True;
        return True;
          
instance=Solution();
print instance.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]); 