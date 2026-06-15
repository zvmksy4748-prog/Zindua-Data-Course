# Rate Limiting & Ethics
# APIs cost money to run. If you put a request inside a while True loop, you are performing a Denial of Service (DoS) attack.
# Use time.sleep() to pause between requests.
import time
import requests

for i in range(5):
    requests.get(f"https://api.example.com/data/{i}")
    print(f"Fetched page {i}")
    time.sleep(1) # Pause for 1 second to be polite