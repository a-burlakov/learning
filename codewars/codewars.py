# # test.assert_equals(find_even_index([1,2,3,4,3,2,1]),3)
# # test.assert_equals(find_even_index([1,100,50,-51,1,1]),1,)
# # test.assert_equals(find_even_index([1,2,3,4,5,6]),-1)
# # test.assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
# # test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
# def codewars(arr: list[int]) -> int:
#     sum_left = 0
#     sum_right = sum(arr)
#
#     for i, number in enumerate(arr):
#         sum_left += number
#         sum_right -= number
#         if sum_left - number == sum_right:
#             return i
#
#     return -1
#
#
# codewars([20, 10, 30, 10, 10, 15, 35])
