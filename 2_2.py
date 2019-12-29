def get_sorted_squares(nums):
    nums = [(x ** 2) for x in nums]
    return sorted(nums)


nums = list(map(int, input().split(', ')))
get_sorted_squares(nums)
