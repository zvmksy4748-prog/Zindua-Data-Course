# If Statements

#There is no limit on the number of statements in the body, but there must be at least one.
# If you haven't written the code yet, use the pass statement as a placeholder:

x = int(input("Enter a value of x:"))
y = int(input("Enter value of y:"))
if x < 0:
    pass # Placeholder: need to handle negative values later

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    elif x > y:
        print('x is greater than y')
    else:
        pass