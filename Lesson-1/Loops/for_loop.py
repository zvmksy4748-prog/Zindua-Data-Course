# For Loop

'''
    Indefinite Loops (while): They run until a condition changes. They are like saying,
        "Keep scrubbing the floor until it is clean." (You don't know exactly how many scrubs it will take).
    Definite Loops (for): They run a specific number of times based on a set of items.
        They are like saying, "Scrub these 5 specific tiles."
'''

temps = [-5, 2, 0, 15, -1, 10]

# Write your loop here
for t in temps:
    if t > 0:
        print(str(t) + "°C is above freezing.")
    else:
        print(str(t) + "°C is freezing!")