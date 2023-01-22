
def codewars(number: int, awesome_phrases: list[int]) -> int:
    for number_to_check, points in {number: 2, number + 1: 1,
                                    number + 2: 1}.items():

        if number_to_check < 100:
            continue

        # Any digit followed by all zeros: 100, 90000
        if len(str(number_to_check)) - len(
                str(number_to_check).rstrip('0')) > 1:
            return points

        # Every digit is the same number: 1111
        if len(set(str(number_to_check))) == 1:
            return points

        # The digits are sequential, incementing†: 1234
        if str(number_to_check) in '1234567890':
            return points

        # The digits are sequential, decrementing‡: 4321
        if str(number_to_check) in '9876543210':
            return points

        # The digits are a palindrome: 1221 or 73837
        if str(number_to_check) == str(number_to_check)[::-1]:
            return points

        # The digits match one of the values in the awesome_phrases array
        if number_to_check in awesome_phrases:
            return points

    return 0


print(codewars(98, [1337, 256]))
