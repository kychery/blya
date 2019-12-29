def get_two_sum(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)-1):
            if int(nums[i]) + int(nums[j]) == k:
                return [i, j]

            
nums = input("nums = ").split(', ')
k = int(input("target = "))
print(get_two_sum(nums, k))
