class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def validation(unit):
            seen = set()

            for num in unit:
                if num == ".":
                    continue

                if num in seen:
                    return False

                seen.add(num)

            return True

        for row in board:
            if not validation(row):
                return False

        for col in range(9):
            column = []

            for row in range(9):
                column.append(board[row][col])

            if not validation(column):
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):

                box = []

                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        box.append(board[row][col])

                if not validation(box):
                    return False
                    
        return True
        