# Sets Operations

'''
The "Operator vs. Method" Rule

For every operation below, Python provides two syntaxes:
    Operator (e.g., |, &): Both operands must be sets.
    Method (e.g., .union()): The argument can be any iterable (list, tuple, range).
        Python converts it to a set internally before the operation.
'''

A = {1, 2}
B = {2, 3}
print(A | B)       # {1, 2, 3}
print(A.union(B))  # {1, 2, 3}

C = {1, 2, 3}
D = {2, 3, 4}
print(C & D) # {2, 3}
print(C.intersection(D)) # {2, 3}

E = {1, 2, 3}
F = {2, 3, 4}
print(E - F) # {1} (Items in A that are not in B)
print(E.difference(F)) # {1} (Items in A that are not in B)

G = {1, 2, 3}
H = {2, 3, 4}
print(G ^ H) # {1, 4} Returns elements present in A or B, but not both.
print(G.symmetric_difference(H)) # {1, 4} Returns elements present in A or B, but not both.

'''
isdisjoint(): Returns True if sets have zero common elements.
issubset() (<=): Returns True if all elements of A are inside B.
issuperset() (>=): Returns True if A contains all elements of B.
'''
small = {1, 2}
big = {1, 2, 3, 4}

print(small.issubset(big))   # True
print(big.issuperset(small)) # True
print(small.isdisjoint(big)) # False (They share 1 and 2)