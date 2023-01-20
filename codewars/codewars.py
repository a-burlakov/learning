import itertools


def codewars(message: str) -> str:

    cipher = ''
    lower_start = ord('a')
    lower_end = ord('z')
    upper_start = ord('A')
    upper_end = ord('Z')
    for symbol in message:

        if not symbol.isalpha():
            cipher += symbol
            continue

        symbol_code = ord(symbol)

        if symbol.islower() and symbol_code + 13 > lower_end:
            new_symbol = chr(lower_start + (13 - lower_end + symbol_code) - 1)
        elif symbol.isupper() and symbol_code + 13 > upper_end:
            new_symbol = chr(upper_start + (13 - upper_end + symbol_code) - 1)
        else:
            new_symbol = chr(symbol_code + 13)

        cipher += new_symbol

    return cipher

