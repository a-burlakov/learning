
def codewars(a, b):
    if a > b:
        a, b = b, a

    return sum([x for x in range(a, b + 1)])


result = codewars(0, -1)

print(result)

