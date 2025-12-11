import requests
import json

# 1. Internet-la irukka oru Dummy API (JSONPlaceholder)
url = "https://jsonplaceholder.typicode.com/users/1"

print(f"Connecting to {url}...")

# 2. Request Anuppurom (GET Request)
# Ithu thaan "Browser" pandra velai, aana code moolama pandrom
response = requests.get(url)

# 3. Check Status (200 na Success, 404 na Not Found)
print(f"Status Code: {response.status_code}")

if response.status_code == 200:
    # 4. Data-va eduthu azhaga print pannu
    data = response.json()
    print("\nData Received from Server:")
    print(f"Name: {data['name']}")
    print(f"Email: {data['email']}")
    print(f"City: {data['address']['city']}")
else:
    print("Something went wrong!")