# Lists Advanced Concepts

# Functions
nums = [3, 41, 12, 9, 74, 15]
print(len(nums)) # 6
print(max(nums)) # 74
print(min(nums)) # 3
print(sum(nums)) # 154

numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)


# It is important to distinguish between operations that modify lists and operations that create new lists.
# For example, the append method modifies a list, but the + operator creates a new list:
t1 = [1, 2]
t2 = t1.append(3)
print(t1) # [1, 2, 3]
print(t2) # None

t3 = t1 + [4]
print(t1) # [1, 2, 3]
print(t3) # [1, 2, 3, 4]

# Objects and values
a = 'banana'
b = 'banana'
print(a is b) # Output: True

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) # Output: False