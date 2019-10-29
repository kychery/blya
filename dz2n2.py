def get_sorted_squares(nums):
    nums = [(x ** 2) for x in nums]
    nums.sort()
    return nums
    

nums = list(map(int, input().split(',')))
get_sorted_squares(nums)
