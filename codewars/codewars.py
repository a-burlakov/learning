def codewars(walk: list):
    return len(walk) == 10 \
           and walk.count('s') == walk.count('n') \
           and walk.count('e') == walk.count('w')


print(codewars(['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's']))
