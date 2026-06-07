# Lists , a list is a sequence of values. []

cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [17, 123]
empty = []
nested_list = ['spam', 2.0, 5, [10, 20]]

# Lists are mutable
# The syntax for accessing the elements of a list is the same as for accessing the characters of a string: the bracket operator.
print(cheeses[0])
numbers[1] = 5
print(numbers)
print('Edam' in cheeses)  # True
print('Brie' in cheeses)  # False

# Traversing a list
# The most common way to traverse the elements of a list is with a for loop.
for cheese in cheeses:
    print(cheese)

values = [1, 2, 3, 4, 5]
print(range(len(values)))
for i in range(len(values)):
    values[i] = values[i] * 2

print(values)
# Output: [2, 4, 6, 8, 10]