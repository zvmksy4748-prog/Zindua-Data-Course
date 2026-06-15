# Consuming Apis

# Get Request - This is how we retrieve data. We will analyze every line of a professional request.
import requests

# 1. The Endpoint
# This is the exact address of the resource we want.
url = "https://jsonplaceholder.typicode.com/users/1"

# 2. The Execution
# Python sends the packet across the internet and waits (blocks)
# until the server replies.
response = requests.get(url)

# 3. The Response Object
# 'response' is NOT the data. It is an object containing the data, headers, and time.
print(f"Server replied with: {response.status_code}")

# 4. Extracting Data
# .text gives us the raw string (useful for HTML)
# .json() parses the string into a Python Dictionary (CRITICAL STEP)
if response.status_code == 200:
    data = response.json()

    # Now we use standard Python Dictionary syntax
    print(f"Name: {data['name']}")
    print(f"City: {data['address']['city']}")  # Nested access
    print(f"Company: {data['company']['name']}")
    print(data)
else:
    print("Request failed.")

# Handling Query Parameters
base_url = "https://jsonplaceholder.typicode.com/posts"

# We want posts by User ID 1 that are NOT completed.
# This mimics: .../posts?userId=1&completed=false
search_criteria = {
    "userId": 1,
    "completed": "false"
}

# requests constructs the full URL automatically
response = requests.get(base_url, params=search_criteria)

print(response.url) # Output: https://jsonplaceholder.typicode.com/posts?userId=1&completed=false