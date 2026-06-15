# Apis Advanced Patterns

import requests
# POST: Creating Data
url = "https://jsonplaceholder.typicode.com/posts"

new_payload = {
    "title": "Mastering Python APIs",
    "body": "This is a detailed guide.",
    "userId": 99
}

# The library automatically adds 'Content-Type: application/json' header
response = requests.post(url, json=new_payload)

if response.status_code == 201:
    print("Success! Created Post ID:", response.json()['id'])
    print(response.status_code)
    print(response.json())

# PUT: Updating Data
url = "https://jsonplaceholder.typicode.com/posts/1"
updated_payload = {
    "id": 1,
    "title": "Updated Title Only",
    "userId": 1
}

response2 = requests.put(url, json=updated_payload)
print(response2.status_code)
print(response2.json())

# DELETE: Removing Data
url = "https://jsonplaceholder.typicode.com/posts/1"
response3 = requests.delete(url) # Usually returns 200 or 204
print(response3.status_code)