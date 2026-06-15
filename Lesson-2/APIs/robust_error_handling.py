# Robust Error Handling

# In the real world, internet connections drop. Servers timeout.
# Using a bare requests.get() is dangerous because if the request fails (e.g., 404),
# the code keeps running and crashes when you try to access .json().

import requests
from requests.exceptions import HTTPError, Timeout

try:
    # timeout=5 ensures the script doesn't freeze forever if server is down
    response = requests.get("https://api.github.com", timeout=5)

    # raise_for_status() checks for 4xx/5xx codes.
    # If bad, it raises an Exception immediately, jumping to 'except'.
    response.raise_for_status()

    data = response.json()
    print("Data retrieved successfully!")

except Timeout:
    print("The server took too long to respond.")
except HTTPError as err:
    print(f"HTTP error occurred: {err}")  # Prints the 404/500 code
except Exception as err:
    print(f"Other error occurred: {err}")