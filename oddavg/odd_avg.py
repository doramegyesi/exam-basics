# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases

#numbers = [1, 2, 3, 4, 5]

def odd_average(numbers = []):
    list_of_numbers = []
    for n in range(len(numbers)):
        if n % 2 != 0:
            list_of_numbers.append(sum(n) / len(n))
        return list_of_numbers

print(odd_average(numbers = [1,2,3]))
