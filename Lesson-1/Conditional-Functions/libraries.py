# Libraries - file containing code that someone else wrote for people to reuse.
# Instead of building those tools from scratch, you import them from a library.

import datetime

# get the current date
now = datetime.datetime.now()
print("Right now it is:", now)
print("Formated date:", now.strftime("%A, %B %d, %Y"))
print("Formated time:", now.strftime("%I:%M %p"))
print("Formated time:", now.strftime("%H:%M:%S"), '\n')

print("The year:",now.year)
print("The month:",now.month)
print("The day:",now.day, "\n")

# OS Library - Operating System
# library allows your Python program to "talk" to your computer's folders and files.
import os

# find out which folder your script is in
where_am_i = os.getcwd()
print('I am running in:', where_am_i)

# list all files in the current folder
files = os.listdir()
print('Files in this folder:', files, '\n')

# Statistics Library
# If you have a list of numbers, you could write a loop to find the average.
# However, the statistics library has "idioms" (patterns) built-in to do this in one line.
import statistics

scores = [85, 93, 45, 87, 93, 72, 81]

print("The average score:", statistics.mean(scores))
print("The middle score:", statistics.median(scores))
print("The most common score:", statistics.mode(scores), "\n")

# The Specific Import
from statistics import mean
print(mean([85, 93, 45, 87, 93, 72, 81]))