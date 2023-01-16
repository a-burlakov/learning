
def codewars(string):

    string = string.lower()

    mexican_wave = []
    for i, symbol in enumerate(string):

        if not symbol.isalpha():
            continue

        mexican_symbols = [chr(ord(s) - 32) if i == j else s for j, s in enumerate(string)]
        mexican_word = ''.join(mexican_symbols)
        mexican_wave.append(mexican_word)

    return mexican_wave

result = codewars('h ello')
