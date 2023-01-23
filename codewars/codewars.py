from functools import reduce

def codewars(n):

    count = 0
    while len(str(n)) > 1:
        n = reduce(lambda i, j: i*j, [int(x) for x in str(n)])
        count += 1

    return count

print(codewars(999))
