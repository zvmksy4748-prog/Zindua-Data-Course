# Parsing Formatting Debugging

# Parsing is the process of analyzing a string to extract specific, meaningful data.
# In the real world, data is rarely clean. It often comes in long "log lines" or messy "headers."

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

# Step 1: Find the @
at_position = data.find('@')
print(at_position) # 21

# Step 2: Find the first space AFTER the @
# Notice we tell find() to start searching at 'at_position'
space_position = data.find(' ', at_position)
print(space_position) # 31

# Step 3: Slice it
# We add 1 to at_position because we don't want the '@' itself
host = data[at_position + 1 : space_position]
print(host) # 'uct.ac.za'


# The Best Practice - Whenever possible, use string methods like .startswith().
# These methods have "built-in" guardians; they return False on empty strings instead of crashing.
line = ""
if line.startswith('#'): # Returns False, no crash!
    print("Comment")