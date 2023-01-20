
def codewars(core_number: int) -> list:
    core_sum = sum(range(1, core_number + 1))

    fit_pairs = []
    for i in range(1, core_number + 1):

        j = (core_sum - i) // i

        if j * i == (core_sum - j - i):
            fit_pairs.append((j, i))
            fit_pairs.append((i, j))

    return sorted(fit_pairs, key=lambda x: x[0])


print(codewars(26))
