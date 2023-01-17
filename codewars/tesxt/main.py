
def codewars(array1, array2):

    return sorted({x for x in array1 if any([x in y for y in array2])})

a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(codewars(a1, a2))
