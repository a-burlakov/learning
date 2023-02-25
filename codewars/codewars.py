# two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]


# test.assert_equals(sorted(two_sum([1,2,3], 4)), [0,2])
# test.assert_equals(sorted(two_sum([1234,5678,9012], 14690)), [1,2])
# test.assert_equals(sorted(two_sum([2,2,3], 4)), [0,1])

def codewars(numbers: list[int], target: int) -> tuple[int, int] | None:

	for i, i_num in enumerate(numbers):
		for j, j_num in enumerate(numbers):
			if i == j: continue
			if i_num + j_num == target:
				return i, j

	return None

print(codewars([1,2,3], 4))