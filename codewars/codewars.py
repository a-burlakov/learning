
def codewars(number_list: list[int]) -> int:
    """
    Returns second after max number from the list.

    :param number_list: list with numbers.
    :return: number that is second after max number in the list.
    """
    max_number = 0
    second_after_max_number = 0
    for number in number_list:
        if max_number < number:
            second_after_max_number = max_number
            max_number = number
        elif second_after_max_number < number:
            second_after_max_number = number

    return second_after_max_number


print(codewars([1, 4, 2, 6, 5]))
print(codewars([5, 3, 1, 2, 4]))
print(codewars([1, 2, 3, 4, 5]))
