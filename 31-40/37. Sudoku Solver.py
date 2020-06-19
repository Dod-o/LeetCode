class Solution(object):
    def _sub_solveSudoku(self, board, cur_fill_x, cur_fill_y, row_list, col_list, rect_list):

        all_filled = False
        next_x, next_y = cur_fill_x, cur_fill_y + 1
        while next_y < 9:
            if board[next_x][next_y] == '.':
                break
            next_y += 1
        if next_y >= 9:
            for x in range(cur_fill_x + 1, 9):
                for y in range(9):
                    if board[x][y] == '.':
                        next_x = x
                        next_y = y
                        break
                if next_y < 9: break
        if next_y >= 9: all_filled = True

        for i in range(1, 10):
            if row_list[cur_fill_x][i] != 1 and col_list[cur_fill_y][i] != 1 and rect_list[cur_fill_x // 3][cur_fill_y // 3][i] != 1:
                board[cur_fill_x][cur_fill_y] = str(i)
                row_list[cur_fill_x][i] = 1
                col_list[cur_fill_y][i] = 1
                rect_list[cur_fill_x // 3][cur_fill_y // 3][i] = 1

                if all_filled == True: return board
                result = self._sub_solveSudoku(board, next_x, next_y, row_list, col_list, rect_list)
                if result != None: return result

                board[cur_fill_x][cur_fill_y] = '.'
                row_list[cur_fill_x][i] = 0
                col_list[cur_fill_y][i] = 0
                rect_list[cur_fill_x // 3][cur_fill_y // 3][i] = 0
        return None

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        row_list = [[0 for __ in range(10)] for _ in range(9)]
        col_list = [[0 for __ in range(10)] for _ in range(9)]
        rect_list = [[[0 for ___ in range(10)] for __ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row_list[i][int(board[i][j])] = 1
                    col_list[j][int(board[i][j])] = 1
                    rect_list[i // 3][j // 3][int(board[i][j])] = 1

        filled_x, filled_y = 0, 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    filled_x = i
                    filled_y = j
                    break
            if board[filled_x][filled_y] == '.': break

        return self._sub_solveSudoku(board, filled_x, filled_y, row_list, col_list, rect_list)


if __name__ == '__main__':
    result = Solution().solveSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
    )
    for i in range(len(result)):
        print(result[i])