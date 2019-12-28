def get_sorted_squares(nums):
    nums = list(map(int, nums))
    squares = [num*num for num in nums]
    return sorted(squares)
    
A = list(input("A = ").split(', '))
get_sorted_squares(A)
          
