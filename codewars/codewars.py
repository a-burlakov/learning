def codewars(sentence: str):

    return ' '.join(sorted(sentence.split(), key=lambda x: [n for n in x if n.isdigit()]))

print(codewars('4of Fo1r pe6ople g3ood th5e the2'))
