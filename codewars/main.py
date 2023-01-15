from collections import Counter

def codewars(text):
    return len([x for x in Counter(text).values() if x > 1])



print(codewars("Indivisibilities"))
