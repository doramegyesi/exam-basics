# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases


def odd_average(numbers = []):
    list_of_numbers = []
    average = 0
    for n in range(len(numbers)):
        if n % 2 != 0:
            list_of_numbers.append(n)
            average = str(sum(list_of_numbers) / len(list_of_numbers))
    return average

print(odd_average(numbers = [1, 2, 3, 4, 5]))
