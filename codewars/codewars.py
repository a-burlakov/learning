def codewars(l: list):

    return int(''.join([str(int(x) ** 2) for x in str(num)]))

print(codewars([1, 2, 'a', 'b']))
