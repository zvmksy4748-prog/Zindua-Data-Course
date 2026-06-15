# Virtual Enviroment

import sys
import os

# This shows where the Python interpreter is currently located
print("Python Interpreter Location:")
print(sys.executable)

# Check if we are in a virtual environment
if hasattr(sys, 'real_prefix') or (sys.base_prefix != sys.prefix):
    print("\nStatus: You are working inside a Virtual Environment!")
else:
    print("\nStatus: You are using the Global System Python.")

# In the next lesson, we will use this:
try:
    import requests
    print("API Library 'requests' is installed and ready!")
except ImportError:
    print("API Library 'requests' not found. Please install it in your env.")