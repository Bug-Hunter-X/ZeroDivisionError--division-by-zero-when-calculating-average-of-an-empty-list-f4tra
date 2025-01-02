def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#More robust solution using exception handling
def calculate_average_robust(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0