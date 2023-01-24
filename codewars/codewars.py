def codewars(s: str):

    if len(s) % 2 == 0:
        return s[len(s) // 2 - 1:len(s) // 2 + 1]
    else:
        return s[len(s) // 2:len(s) // 2 + 1]

print(codewars('4of Fo1r pe6ople g3ood th5e the2'))
