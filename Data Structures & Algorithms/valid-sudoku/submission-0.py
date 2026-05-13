class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [["."]*9 for _ in range(9)]

        for i, row in enumerate(board):
            for j in range(9):
                columns[j][i] = row[j]

            row_filtered = [x for x in row if x != "."]
            if len(row_filtered) != len(set(row_filtered)):
                return False

        for i, column in enumerate(columns):
            column_filtered = [x for x in column if x != "."]
            if len(column_filtered) != len(set(column_filtered)):
                return False

        areas = [[] for _ in range(9)]
        for i in range(9):
            areas[(i // 3) * 3 + 0].extend(board[i][0:3])
            areas[(i // 3) * 3 + 1].extend(board[i][3:6])
            areas[(i // 3) * 3 + 2].extend(board[i][6:9])

        for area in areas:
            area_filtered = [x for x in area if x != "."]
            if len(area_filtered) != len(set(area_filtered)):
                return False

        return True