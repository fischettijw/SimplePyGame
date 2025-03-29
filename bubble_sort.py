import os; os.system("cls")

def ascending_bubble_sort_in_place(nums):   # docstring 
    """
    Sorts a list of numbers in place using the bubble sort algorithm.

    Args:
        nums (list): The list of numbers to sort.

    Returns:
        None
    """
    n = len(nums)
    for i in range(n-1):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                # Swap nums[j] and nums[j+1]
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                # nums[j], nums[j+1] = nums[j+1], nums[j]

numbers = [45,23,99,3,56,39,4,12,67]
print(numbers)

ascending_bubble_sort_in_place(numbers)
print(numbers)

print()