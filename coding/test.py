import math


def is_satisfied(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print(math.fabs(i - j))
            if nums[i] == nums[j] and math.fabs(i - j) <= k:
                return True
    return False


print(is_satisfied([1, 2, 3, 1, 2, 3], 2))
nums = [1, 2, 3, 1, 2, 3]

