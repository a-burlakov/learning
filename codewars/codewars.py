def codewars(triplets: [list[list[str]]]) -> str:

    secret_word = ''
    while any(x for x in triplets):

        first_letters = [x[0] for x in triplets if x]
        for first_letter in first_letters:

            is_first_letter_ever = True

            for triplet in triplets:
                if first_letter in triplet and triplet.index(first_letter) > 0:
                    is_first_letter_ever = False
                    break

            if is_first_letter_ever:
                secret_word += first_letter
                for triplet in triplets:
                    if first_letter in triplet:
                        triplet.remove(first_letter)
                break

    return secret_word


triplets = [
    ['t', 'u', 'p'],
    ['w', 'h', 'i'],
    ['t', 's', 'u'],
    ['a', 't', 's'],
    ['h', 'a', 'p'],
    ['t', 'i', 's'],
    ['w', 'h', 's']
]

print(codewars(triplets))
