# a = [1, 2, 3, 4, 5]
# sqred_lst = [x * x for x in a]
# sqred_lst.sort(reverse=True)
# for idx in range(len(sqred_lst)):
#     left = idx + 1
#     right = len(sqred_lst) - 1
#     target = sqred_lst[idx]
#     while left < right:
#         current_sum = sqred_lst[left] + sqred_lst[right]
#         print(current_sum)
#         if current_sum == target:
#             print("Triplet found!!", target, sqred_lst[left], right)
#             left += 1
#             right -= 1
#         elif target > current_sum:
#             right -= 1
#         else:
#             left += 1
# a=10.1
# b=10.1
# print(a is b)
for idx, value in enumerate(["a","b"]):
    print(f"I am file {idx+1}",value)
