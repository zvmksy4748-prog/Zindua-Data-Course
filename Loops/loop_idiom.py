# Loop Idioms

count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
    #count = count + itervar
print('Count: ', count)

# Maximum and Minimum Loops
# To find the largest value in a list or sequence, we construct the following loop:
largest = None
print('Before:', largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    # if largest is None then we take the first value we see as the largest so far.
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)

# To find the smallest value in a list or sequence, we construct the following loop:
smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print('Smallest:', smallest)

def min(values):
    small = None
    for value in values:
        if small is None or value < small:
            small = value
    return small