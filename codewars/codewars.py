from collections import defaultdict

def codewars(n):

    count_dict = defaultdict(int)
    for number in n:
        count_dict[number] += 1

    return [k for k, v in count_dict.items() if v == 1][0]

print(codewars([ 0, 0, 0.55, 0, 0 ]))
