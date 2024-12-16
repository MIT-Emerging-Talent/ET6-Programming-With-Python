def sum_even_and_odd_numbers(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if isinstance(num, (int, float)):  # Check if the element is a number
            if num % 2 == 0:
                even_sum += num
            else:
                odd_sum += num
    return even_sum, odd_sum


# Example usage:
# result = sum_even_and_odd_numbers([1, 'a', 2, 'b', 3, 'c'])
# print(result)  # Output: (2, 4)
