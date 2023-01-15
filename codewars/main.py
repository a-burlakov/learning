def codewars(text):
    parentheses = ''.join([x for x in text if x in ['(', ')']])

    while parentheses:
        first_close = parentheses.find(')')
        first_open = parentheses.find('(')

        if first_close < 0 or \
                first_open < 0 or \
                first_open > first_close:
            return False

        for i in sorted([first_open, first_close], reverse=True):
            parentheses = parentheses[:i] + parentheses[i + 1:]

    return True

print(codewars("((sd))(((ff)qr(eq))(rwer))"))
