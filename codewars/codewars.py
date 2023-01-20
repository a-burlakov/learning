
def codewars(dice: list[int]) -> int:

    numbers_line = ''.join([str(x) for x in sorted(dice)])

    points_table = {
        '111': 1000,
        '666': 600,
        '555': 500,
        '444': 400,
        '333': 300,
        '222': 200,
        '5': 50,
        '1': 100,
    }

    points = 0
    for sequence, points_for_sequence in points_table.items():

        while sequence in numbers_line:
            numbers_line = numbers_line.replace(sequence, '', 1)
            points += points_for_sequence

    return points


print(codewars([2, 3, 4, 6, 2]))
print(codewars([4, 4, 4, 3, 3]))
print(codewars([2, 4, 4, 5, 4]))
