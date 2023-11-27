def find_largest_number(numbers):
    if not numbers:
        return None  # Handle empty list case
    else:
        return max(numbers)

# Example usage:
my_list = [4, 7, 1, 9, 3, 5]
largest_number = find_largest_number(my_list)
print(f"The largest number in the list is: {largest_number}")


