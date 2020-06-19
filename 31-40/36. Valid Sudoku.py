class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        for i in range(9):
            num_dict = [0 for _ in range(10)]
            for j in range(9):
                if board[i][j] == '.': continue
                if num_dict[int(board[i][j])] == 1: return False
                num_dict[int(board[i][j])] += 1

        for j in range(9):
            num_dict = [0 for _ in range(10)]
            for i in range(9):
                if board[i][j] == '.': continue
                if num_dict[int(board[i][j])] == 1: return False
                num_dict[int(board[i][j])] += 1

        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                num_dict = [0 for _ in range(10)]
                for k in range(3):
                    for v in range(3):
                        if board[i + k][j + v] == '.': continue
                        if num_dict[int(board[i + k][j + v])] == 1: return False
                        num_dict[int(board[i + k][j + v])] += 1
        return True




if __name__ == '__main__':
    result = Solution().isValidSudoku(
        [[".", ".", ".", ".", "5", ".", ".", "1", "."],
         [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"],
         ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."],
         [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."],
         [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]
)
    print(result)