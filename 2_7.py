def get_two_sum(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for l in range(j+1, len(nums)):
                if int(nums[i]) + int(nums[j]) + int(nums[l]) == k:
                    return [i, j, l]

            
nums = input("nums = ").split(', ')
k = int(input("target = "))
print(get_two_sum(nums, k))
