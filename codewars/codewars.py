class Sudoku(object):
    def __init__(self, board):
        self.board = board
        pass

    def is_valid(self):

        # Checking sudoku format.
        size = len(self.board[0])
        if len(self.board) != size or any([len(row) != size for row in self.board]):
            return False

        for row in self.board:
            for n in row:
                if not type(n) is int:
                    return False

        sa = int(size ** 0.5)

        subgrids = []
        for i in range(sa):
            for j in range(sa):
                subgrid = []
                for z in range(sa):
                    subgrid.extend(self.board[j * sa + z][i * sa:i * sa + sa])
                subgrids.append(subgrid)

        # Checking rows, columns and subgrids.
        numbers_collections = [self.board, zip(*self.board), subgrids]
        for numbers_collection in numbers_collections:
            for numbers in numbers_collection:
                if 0 in numbers or len(set(numbers)) != size:
                    return False

        return True


badSudoku2 = Sudoku([[2]])

print(badSudoku2.is_valid())