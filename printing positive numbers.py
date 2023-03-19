def print_positive_numbers(numbers):
    positive_numbers = []
    for num in numbers:
        if num > 0:
            positive_numbers.append(num)
    print(positive_numbers)
    

list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

print_positive_numbers(list1)  # Output: [12, 5, 64]
print_positive_numbers(list2)  # Output: [12, 14, 3]
