import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users"

try:
    # Fetch data from API
    response = requests.get(url)

    # Check for successful response
    response.raise_for_status()

    # Convert JSON response into Python data
    users = response.json()

    print("USER DETAILS\n")

    # Display user information
    for user in users:
        print(f"ID: {user['id']}")
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"City: {user['address']['city']}")
        print("-" * 30)

    # Filtering logic
    print("\nUsers from South Christy:\n")

    for user in users:
        if user['address']['city'] == "South Christy":
            print(user['name'])

# Error handling
except requests.exceptions.RequestException as e:
    print("Error fetching data:")
    print(e)