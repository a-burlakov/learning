def codewars(s):
    return '-'.join(''.join([x for _ in range(i+1)]).title() for i, x in enumerate(s))


print(codewars('RqaEzty'))
