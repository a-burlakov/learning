def codewars(n, p):

    sum_of_powers = sum([int(x) ** (i + p) for i, x in enumerate(str(n))])
    k = sum_of_powers / n
    if k.is_integer():
        return k
    else:
        return -1


def tests():

    assert codewars(46288, 3) == 51

tests()
