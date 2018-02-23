class Solution(object):
    # [[".", "8", "7", "6", "5", "4", "3", "2", "1"],
    #  ["2", ".", ".", ".", ".", ".", ".", ".", "."],
    #  ["3", ".", ".", ".", ".", ".", ".", ".", "."],
    #  ["4", ".", ".", ".", ".", ".", ".", ".", "."],
    #  ["5", ".", ".", ".", ".", ".", ".", ".", "."],
    #  ["6", ".", ".", ".", ".", ".", ".", ".", "."],
    #  ["7", ".", ".", ".", ".", ".", ".", ".", "."],
    #  ["8", ".", ".", ".", ".", ".", ".", ".", "."],
    #  ["9", ".", ".", ".", ".", ".", ".", ".", "."]]
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # if not self.horizontalBool(board):
        #     return False
        # # if not self.verticalBool(board):
        # #     return False
        # if not self.nineGridBool(board):
        #     return False
        # return True
        for i in range(len(board)):
            temp1 = ['.']*9
            temp2 = ['.']*9
            temp = ['.']*9
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    horizontalnum = ord(board[i][j])-ord('0')-1
                    if temp1[horizontalnum] == '.':
                        temp1[horizontalnum] = board[i][j]
                    else:return False
                if board[j][i] != '.':
                    verticalnum = ord(board[j][i])-ord('0')-1
                    if temp2[verticalnum] == '.':
                        temp2[verticalnum] = board[j][i]
                    else:return False
                s = board[j / 3 + 3 * (i / 3)][j % 3 + 3 * (i % 3)]
                if s != '.':
                    num = ord(s) - ord('0') - 1
                    if temp[num] == '.':
                        temp[num] = s
                    else:
                        return False
        return True


    # def horizontalBool(self,board):
    #     for i in range(len(board)):
    #         temp1 = ['.']*9
    #         for j in range(len(board[i])):
    #             if board[i][j] != '.':
    #                 horizontalnum = ord(board[i][j])-ord('0')-1
    #                 if temp1[horizontalnum] == '.':
    #                     temp1[horizontalnum] = board[i][j]
    #                 else:return False
    #     return True
    # def verticalBool(self,board):
    #     a = [[]for i in board[0]]
    #     for i in board:
    #         for j in range(len(i)):
    #             a[j].append(i[j])
    #     return self.horizontalBool(a)
    # def nineGridBool(self,board):
    #     for i in range(9):
    #         temp = ['.'] * 9
    #         for j in range(9):
    #             s = board[j/3+3*(i/3)][j%3+3*(i%3)]
    #             if s!='.':
    #                 num = ord(s)-ord('0')-1
    #                 if temp[num] == '.':
    #                     temp[num] = s
    #                 else:return False
    #     return True
if __name__ == '__main__':
    s = Solution()
    # print s.horizontalBool([[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]])
    # print s.verticalBool([[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]])
    # print s.nineGridBool([[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]])
    print s.isValidSudoku([[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]])