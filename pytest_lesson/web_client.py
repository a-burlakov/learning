
def codewars(dna):
    complements = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    other_side = ''
    for symbol in dna:
        if symbol in complements:
            other_side += complements[symbol]
        else:
            other_side += symbol

    return other_side


result = codewars('TAACG')

print(result)

