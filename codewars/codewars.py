def codewars(a: list[int], b: list[int]) -> list:

    for number_to_delete in b:

        while number_to_delete in a:
            a.remove(number_to_delete)

    return a


print(codewars([1,2,2], []))
