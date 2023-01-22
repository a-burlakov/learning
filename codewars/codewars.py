
def codewars(string):

    if not string:
        return True

    return all([string.lower().count(x.lower()) == 1 for x in string])


print(codewars("mOose"))
