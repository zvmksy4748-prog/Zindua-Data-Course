# Lists Operations Methods

# Operations +
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c) # Output: [1, 2, 3, 4, 5, 6]

# Operations *
print([0] * 4) # Output: [0, 0, 0, 0]
print([1, 2, 3] * 3) # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Operations slices
t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])  # ['b', 'c']
print(t[:4])   # ['a', 'b', 'c', 'd']
print(t[3:])   # ['d', 'e', 'f']

# Methods
t.append('g')
print(t)#  Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g']

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1) # Output: ['a', 'b', 'c', 'd', 'e']

t3 = ['d', 'c', 'e', 'b', 'a']
t3.sort()
print(t3) # Output: ['a', 'b', 'c', 'd', 'e']

# Deleting items
# There are several ways to overhead elements from a list.
y = ['a', 'b', 'c']
x = y.pop(1)
print(y) # ['a', 'c']
print(x) # 'b'

# If you don’t need the removed value
num = ['a', 'b', 'c']
del num[1]
print(num) # ['a', 'c']

num1 = ['a', 'b', 'c', 'd', 'e', 'f']
del num1[1:5]
print(num1) # Output: ['a', 'f']

# If you know the element you want to remove (but not the index)
num2 = ['a', 'b', 'c']
num2.remove('b')
print(num2) # ['a', 'c']