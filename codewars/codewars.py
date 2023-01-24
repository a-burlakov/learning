def codewars(board: list[list[int]]) -> bool:
    subgrids = []
    for i in range(3):
        for j in range(3):
            subgrids.append(board[j * 3 + 0][i * 3:i * 3 + 3] +
                            board[j * 3 + 1][i * 3:i * 3 + 3] +
                            board[j * 3 + 2][i * 3:i * 3 + 3])

    # Checking rows, columns and subgrids.
    numbers_collections = [board, zip(*board), subgrids]
    for numbers_collection in numbers_collections:
        for numbers in numbers_collection:
            if 0 in numbers or len(set(numbers)) != 9:
                return False

    return True


print(codewars([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 9, 6, 1, 7, 9]]))
