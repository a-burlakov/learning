import itertools


def codewars(observed: str) -> list[str]:
    # ┌───┬───┬───┐
    # │ 1 │ 2 │ 3 │
    # ├───┼───┼───┤
    # │ 4 │ 5 │ 6 │
    # ├───┼───┼───┤
    # │ 7 │ 8 │ 9 │
    # └───┼───┼───┘
    #     │ 0 │
    #     └───┘

    adjacents = {
        '1': ['2', '4', '1'],
        '2': ['1', '3', '5', '2'],
        '3': ['2', '6', '3'],
        '4': ['1', '5', '7', '4'],
        '5': ['2', '4', '6', '8', '5'],
        '6': ['3', '5', '9', '6'],
        '7': ['4', '8', '7'],
        '8': ['5', '7', '9', '0', '8'],
        '9': ['6', '8', '9'],
        '0': ['8', '0'],
    }

    lists = []
    for symb in observed:
        lists.append(adjacents[symb])

    pin_list = []
    for pin in itertools.product(*lists):
        pin_list.append(''.join(pin))

    return pin_list


print(codewars('11'))
